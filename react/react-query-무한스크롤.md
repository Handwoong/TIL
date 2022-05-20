## 무한스크롤?

무한스크롤이란 사용자가 버튼을 누르거나 특정 지점을 스크롤 할 때 새로운 데이터를 가져오는 것이다. 페이스북, 인스타그램의 게시글 피드를 생각하면 된다. 보통 페이지네이션과 무한스크롤 중 고민하게 되는데 상황에 따라 각 방법의 장단점이 있음으로 자신의 서비스에서 어떤 방법을 써야 UX경험이 더 좋을지 고민 해보아야 한다.

**특징**

- 사용자가 데이터의 끝부분으로 스크롤했을 때 끊김 없이 계속 스크롤 가능하다.
- 모든 데이터를 한번에 가져오는 것보다 효율적이다.

무한스크롤을 구현할 때 react-query의 useInfiniteQuery를 사용하면 쉽게 구현 할 수 있다.

## 시작하기 전에

무한스크롤을 구현하기 전에 react-query가 쉽게 이전, 다음 페이지의 여부를 알 수 있도록 백엔드 API세팅이 필요하며, 이때 다음페이지 번호나 페이지 존재 여부, 다음페이지 URL 등 다음페이지를 확인 할 수 있다면 뭐든지 와도 상관없다. 이 글에선 페이지 존재여부를 사용하며 게시글 목록 요청 시 응답 받는 데이터 형식은 아래와 같다.

```js
{
  "isLast": false, // 페이지 존재 여부
  "posts": [ ...postData ]
}
```

isLast라는 boolean값을 받아 현재 페이지가 마지막페이지 인지를 알 수 있다. 이는 뒤에서 사용 할useInfiniteQuery에 옵션으로 isLast의 값에 따라 다음페이지를 불러올 수 있게끔 한다거나 불러오지 못하게 설정한다.

## useInfiniteQuery

useInfiniteQuery도 useQuery와 같이 인자로 쿼리키, 쿼리함수, 옵션을 받으며 useQuery와 다른점으로 이 쿼리함수는 객체 매개변수를 받으며 프로퍼티로 pageParam을 가지고 있다. 이 pageParam의 값에 따라 useInfiniteQuery는 다음페이지에 요청을 보낼 수 있고 마지막페이지라면 pageParam를 undefined로 만들어 요청을 보내지 않게 할 수 있다.

아래는 첫 페이지를 받아오고 나서 inView가 true라면 다음페이지를 받아오는 코드이다. 코드를 보고 자세히 살펴보도록 하자.

```js
import React, { useEffect } from "react";
import { useInView } from "react-intersection-observer";
import { PostsContainer } from "styles/Posts/PostStyle";
import PostCard from "pages/Post/PostCard";
import Loading from "components/Loading";
import ErrorPage from "components/ErrorPage";
import { useInfiniteQuery } from "react-query";
import axios from "axios";

const fetchPostList = async (pageParam) => {
  const res = await axios.get(
    `http://localhost:5001/posts?&page=${pageParam}&limit=6`
  );
  const { posts, isLast } = res.data;
  return { posts, nextPage: pageParam + 1, isLast };
};

function Posts() {
  const { ref, inView } = useInView();
  const { data, status, fetchNextPage, isFetchingNextPage } = useInfiniteQuery(
    "posts",
    ({ pageParam = 1 }) => fetchPostList(pageParam),
    {
      getNextPageParam: (lastPage) =>
        !lastPage.isLast ? lastPage.nextPage : undefined,
    }
  );

  useEffect(() => {
    if (inView) fetchNextPage();
  }, [inView]);

  if (status === "loading") return <Loading />;
  if (status === "error") return <ErrorPage />;

  return (
    <>
      <PostsContainer>
        {data?.pages.map((page, index) => (
          <React.Fragment key={index}>
            {page.posts.map((post) => (
              <PostCard key={post._id} post={post}></PostCard>
            ))}
          </React.Fragment>
        ))}
      </PostsContainer>
      {isFetchingNextPage ? <Loading /> : <div ref={ref}></div>}
    </>
  );
}
export default Posts;
```

무한스크롤을 구현하면서 react-intersection-observer를 사용하였는데 간단하게 설명하자면 DOM 요소에 ref로 모니터링 하고 해당 요소가 화면에 보이는지 안보이는지 여부를 inView로 알 수 있다. react-query 공식문서의 useInfiniteQuery 예제에서도 사용하고 있었고 간편하다보니 예제로 쓰기 좋은 것 같다.

### Query Function

쿼리함수에서 pageParam의 기본값을 정해준다. 이 예제에선 페이지번호를 사용했지만 백엔드 API응답이 다음페이지의 URL을 준다면 요청URL을 기본값으로 사용해도 된다.

```js
({ pageParam = 1 }) => fetchPostList(pageParam);
```

별 다를 것 없는 fetch함수이다. 반환값으로 nextPage라는 프로퍼티를 만들어 다음페이지 번호를 넣어주었다. 여기서 실제 사용할 데이터인 posts와 isLast, nextPage를 return하였는데 이 반환값을 useInfiniteQuery의 옵션으로 준 getNextPageParam에서 매개변수로 받을 수 있게된다.

```js
const fetchPostList = async (pageParam) => {
  const res = await axios.get(
    `http://localhost:5001/posts?&page=${pageParam}&limit=6`
  );
  const { posts, isLast } = res.data;
  return { posts, nextPage: pageParam + 1, isLast };
};
```

### Options

useInfiniteQuery의 옵션으로 getNextPageParam을 사용하였다. 위에서 말했듯 fetch함수에서 반환한 값을 매개변수로 받아오고 마지막페이지인지 여부에따라 pageParam을 다음페이지 번호 또는 undefined로 설정한다.

```js
{
  getNextPageParam: (lastPage) =>
    !lastPage.isLast ? lastPage.nextPage : undefined,
}
```

### return

useInfiniteQuery에서 반환된 data는 useQuery와 다른 프로퍼티를 가지고 있다. useQuery의 data 객체는 단순히 쿼리함수에서 반환된 데이터라면 useInfiniteQuery의 data는 pages와 pageParams 프로퍼티를 가진다. pages에는 각 페이지들이 쿼리함수에서 반환한 데이터들이 배열로 들어가며, pageParams에는 각 페이지의 pageParam값이 들어있다.

예로 스크롤을 내려 2번째 페이지까지 요청한 data의 프로퍼티는 다음과 같다.

```js
{
  "pages": [
      {
          "posts": [ ...firstPagePosts ],
          "nextPage": 2,
          "isLast": false
      },
      {
          "posts": [ ...secondPagePosts ],
          "nextPage": 3,
          "isLast": false
      }
  ],
  "pageParams": [
      null,
      2
  ]
}
```

이 외에도 fetchNextPage, hasNextPage, isFetchingNextPage들을 반환하는데 이름만 봐도 알 수 있기 때문에 자세한 건 공식문서를 참고하자.

> useInfiniteQuery : https://react-query.tanstack.com/guides/infinite-queries

## 마치며

처음에 공식문서를 보면서 무한스크롤을 구현하였는데 꼼꼼하게 안읽고 휙휙 넘기다보니 이해가 안되서 많은 시간을 써버렸다. 이 글이 다른분들의 시간을 조금이나마 아낄 수 있게 도움이 되었으면 좋겠다.
