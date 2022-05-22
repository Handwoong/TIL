## 왜 React-Query 사용했나?

프로젝트를 진행하면서 좋아요 기능을 구현하게 되었다. 당시 상태관리 라이브러리에 대한 지식이 없기도 하였고 사용할 필요성도 느끼지 못했기 때문에 React에 내장된 Context API를 사용해서 구현하였다. Context가 상태관리를 위한 도구라고 생각했었고 이 생각에 문제가 있다는 것을 좋아요를 누르고 취소할 때마다 전역상태로 사용되는 유저상태를 변경, 모든 컴포넌트가 다시 렌더링되는 현상을 목격하면서 알게 되었다.

원인을 알기위해 Context API의 공식문서를 확인해보니 다음과 같이 나와있었다. `Provider의 부모가 렌더링 될 때마다 불필요하게 하위 컴포넌트가 다시 렌더링 되는 문제가 생길 수도 있습니다.` 이는 결국 Context.Provider에서 상태를 업데이트하면 하위 컴포넌트들이 재렌더링 된다라는 말이었고 생각해보면 당연한 동작원리였다.

문제 원인인 Context로 상태관리를 하게 되면 렌더링 성능을 보장할 수 없다는 것을 알게 되었고 해결을 위해 프로젝트 내에서 전역적으로 사용하는 상태들이 서버관련 데이터 위주임을 확인하고 서버상태관리 라이브러리라고 알려진 React-Query를 알아보게 되었다.

## React-Query 소개

react-query는 서버 상태를 관리하는 라이브러리이다. 여기서 상태는 크게 클라이언트 상태와 서버 상태로 나눌 수 있다.

- 클라이언트 상태는 웹 브라우저 세션과 관련된 모든 정보 예를 들어 다크모드는 서버와 상관 없이 클라이언트에서 관리하는 상태이다.

- 서버 상태는 클라이언트에서 서버에 저장되어 있는 데이터를 사용 하는 것이라고 할 수 있다. 예를들어 게시물 데이터, 댓글 데이터 등이 있다.

리액트 앱에서 서버의 데이터가 필요 할 때 바로 서버로 요청을 보내는 것이 아니라 react-query에 캐싱되어 있는 데이터가 있는지 먼저 확인하고, 있으면 캐싱된 데이터를 없으면 요청을 보내고 데이터를 캐싱한다.

![structure](https://velog.velcdn.com/images/handwoong/post/c223198b-0d3f-4046-a564-881474f5bb7b/image.jpeg)

### React-Query를 사용하는 이유

- 캐싱
- 서버의 데이터를 가져오는 중 loading 및 error 상태를 쉽게 처리가능
- API 요청 중 동일한 요청이 있다면 중복요청 방지
- 페이지네이션 및 무한스크롤
- 사용자가 필요하다고 예상되는 데이터를 prefetch
- API 코드의 분리

이처럼 react-query는 클라이언트에서 서버 데이터를 캐싱하고 관리해주는 라이브러리이다.

## 사용하기

react-query를 본격적으로 사용하기에 앞서 쿼리와 서버 데이터 캐시를 관리하는 클라이언트를 생성한다.
react-query는 내부적으로 Context API를 사용하며 Context와 같이 Provider로 하위 컴포넌트들이 생성한 클라이언트를 사용 할 수 있게 감싸주어야 한다.

```js
import Example from "./Example";
import { QueryClient, QueryClientProvider } from "react-query";

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <div className="App">
        <Example />
      </div>
    </QueryClientProvider>
  );
}

export default App;
```

이제 `QueryClientProvider`내의 하위 컴포넌트에서 react-query hook들과 쿼리 클라이언트가 가지고 있는 캐시와 모든 옵션들을 사용할 수 있게 되었다.

### useQuery

useQuery는 서버에서 데이터를 가져올 때 사용하는 hook이다.
useQuery는 인자로 쿼리키(쿼리이름), 쿼리함수, 옵션을 받으며 여기서 쿼리함수는 데이터를 불러오는 비동기 함수를 넣어주면 된다.

아래는 todo목록을 불러오는 예제이다.

```js
import axios from "axios";
import { useQuery } from "react-query";

async function fetchTodoList() {
  const res = await axios.get("https://jsonplaceholder.typicode.com/todos");
  return res.data;
}

function Example() {
  const { data, isLoading, isError, error } = useQuery("todos", fetchTodoList);

  if (isLoading) return <div>Loading...</div>;
  if (isError) return <div>{error.toString()}</div>;

  return (
    <div>
      <ul>
        {data.map((todo) => (
          <li key={todo.id}>{todo.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default Example;
```

useQuery는 data, isLoading, isError, isFetching 등을 반환하게 된다. 이는 공식문서에서 확인 할 수 있다. 여기서 중요한 점은 데이터를 가져오는 중에 `data`는 undefined이기 때문에 isLoading을 빼놓지 말고 꼭 써주자.

> useQuery : https://react-query.tanstack.com/reference/useQuery

### isLoading과 isFetching

isLoading과 isFetching은 둘 다 서버의 데이터를 가져오는 중인지를 나타내는 boolean값이다. 다만 isLoading은 캐싱되어 있는 데이터가 없으면 서버의 데이터를 가져오게 되면서 true가 되고 isFetching은 매번 서버의 데이터를 가져올 때마다 true가 된다.

isLoading 예
![isLoading](https://velog.velcdn.com/images/handwoong/post/6399a605-ce0f-4c88-ba13-513267e9b2de/image.gif)

isFetching 예
![isFetching](https://velog.velcdn.com/images/handwoong/post/1ebd3add-8247-4485-8efb-0fa6dfccadee/image.gif)

위의 예제를 보면 알 수 있는 것은 isLoading의 경우 fetch중에 캐싱되어 있는 데이터를 먼저 보여주고 fetch가 완료되면 자연스럽게 렌더링이 되는 반면 isFetching은 fetch중에 Loading 컴포넌트가 보이고나서 렌더링이 되는 것을 확인 할 수 있다.
뭐가 더 좋다고 할 수 없지만 자신이 원하는 동작에 맞춰 사용하면 된다.

### error와 isError

isError는 서버의 데이터를 받아오던 중 에러가 발생하였는지 나타내는 boolean값이다. 또한 error객체를 통해 에러에 대한 정보를 알 수 있다.

![error-object](https://velog.velcdn.com/images/handwoong/post/e4bbeee5-734c-4550-99c0-cfb174c0bd02/image.png)

### React-Query DevTools

react-query는 캐싱되어 있는 데이터를 확인하기 쉽게 devtools를 제공한다. 공식문서를 보면 `process.env.NODE_ENV === 'development'`일 때만 devtools를 포함한다고 하는데 리액트 앱을 build하게 되면 `process.env.NODE_ENV === 'production'`이 됨으로 서비스 배포 시 devtools컴포넌트가 보일까 하는 부분에 대해 걱정 할 필요가 없다.

사용방법은 아래 코드와 같이 간단하게 사용할 수 있다.

```js
import Example from "./Example";
import { QueryClient, QueryClientProvider } from "react-query";
import { ReactQueryDevtools } from "react-query/devtools";

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <div className="App">
        <Example />
      </div>
      <ReactQueryDevtools />
    </QueryClientProvider>
  );
}

export default App;
```

앱을 실행시켜보면 왼쪽 하단에 react-query의 로고모양이 생기고 누르게 되면 아래 사진과 같이 쿼리에 대한 정보와 refetch, invalidate, remove와 같은 도구를 제공함으로써 손쉽게 데이터를 제어해 볼 수 있다.

![devtools](https://velog.velcdn.com/images/handwoong/post/f769954e-e7c0-4f68-8bf5-6d29001c4adc/image.png)

devtools에서 확인가능한 정보는 다음과 같다.

- 쿼리키와 쿼리의 상태(fresh, stale, inactive)
- 쿼리가 업데이트 된 시간
- 캐싱되어 있는 데이터
- 쿼리에 대한 정보(캐싱시간, 적용된 옵션 등)

> DevTools : https://react-query.tanstack.com/devtools

### staleTime, cacheTime

쿼리의 상태는 3가지가 있다. fresh(신선한), stale(신선하지 않은), inactive(사용하지 않는)
중요하게 봐야 할 것은 stale 상태이다. react-query에서 데이터 리패칭은 stale상태에서만 일어난다. 데이터 리패칭을 위한 여러 트리거가 있는데, 컴포넌트 remount, 윈도우 refocus등이 있다.

아래 코드는 위의 todo목록을 불러오는 코드에서 옵션으로 staleTime을 설정해 주는 코드이다.

```js
const { data, isLoading, isError, error } = useQuery("todos", fetchTodoList, {
  staleTime: 5000,
});
```

위의 코드에서 staleTime을 5초로 설정하고(default는 0초) 데이터를 불러오게 되면 처음엔 fresh상태지만 5초 후엔 stale상태로 변하게 된다. 데이터의 유형에 따라 유동적으로 설정하는 것이 필요하다.

cacheTime은 기본적으로 5분으로 설정되어 있고 staleTime과 같이 옵션으로 설정 해 줄 수 있으며 쿼리가 inactive상태에서 캐시에 남아있는 시간을 말한다. 기본 5분이기 때문에 따로 설정해주지 않았다면 inactive상태에서 캐시에 5분간 남아있게 되고 5분이 지났다면 가비지 컬렉션에 의해 삭제된다.

### useMutation

지금까지 useQuery hook을 통해 서버의 데이터를 받아오는 get에 대해 다루었다면 useMutation hook을 통해서는 데이터의 생성/수정/삭제가 가능하다. useMutation을 사용하면 Optimistic 업데이트(대표적으로 좋아요 기능)와 같이 요청이 성공할 것이라 보고 캐시를 미리 업데이트하고 만약 실패한다면 롤백시키는 방법을 간단하게 구현할 수 있다. 그 외에도 요청을 보내고 받은 응답 데이터로 캐시를 업데이트 할 수 있고 관련 데이터들을 무효화 시켜 리패칭을 진행하는 것도 가능하다.

아래 코드는 todo를 클릭하면 삭제하는 예제이다.

```js
import axios from "axios";
import { useQuery, useMutation } from "react-query";

async function fetchTodoList() {
  const res = await axios.get("https://jsonplaceholder.typicode.com/todos");
  return res.data;
}

async function deleteTodo(todoId) {
  await axios.delete(`https://jsonplaceholder.typicode.com/todos/${todoId}`);
}

function Example() {
  const { data, isLoading, isError, error } = useQuery("todos", fetchTodoList, {
    staleTime: 5000,
  });
  const deleteMutation = useMutation(deleteTodo);

  const hadleDeleteTodo = (todoId) => deleteMutation.mutate(todoId);

  if (isLoading) return <div>Loading...</div>;
  if (isError) return <div>{error.toString()}</div>;

  return (
    <div>
      <ul>
        {data.map((todo) => (
          <li key={todo.id} onClick={() => hadleDeleteTodo(todo.id)}>
            {todo.title}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Example;
```

useQuery와 다르게 useMutation은 쿼리키를 생략한다. 그 이유는 캐싱되어 있는 데이터와 상관없이 서버에 저장된 데이터를 생성/수정/삭제 하기 때문이다. 또한 두번째 인자로 옵션을 줄 수 있는데 요청 성공에 대한 작업인 onSuccess, 에러가 났을때는 onError, 성공/실패 상관없이 실행하는 onSetteld등 요청 후 작업들을 정해 줄 수 있다.

> Mutation : https://react-query.tanstack.com/guides/mutations

## 마치며

엘리스 데이터 분석 프로젝트를 진행하면서 사용했던 react-query의 기본 사용법을 정리하였는데 사용하면서 헷갈렸던 staleTime과 cacheTime같은 개념들이 글을 쓰며 정리가 된 것 같다. 프로젝트를 진행하면서 알아봤던 prefetch, 페이지네이션, 무한스크롤 같은 기능들도 정리하면서 찾아보고 기존에 사용했던 방법보다 더 좋은 방법으로 구현이 가능한지 고민해봐야겠다.
