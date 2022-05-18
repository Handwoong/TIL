function solution(id_list, report, k) {
  const reportCount = {};
  const user = id_list.reduce((acc, cur) => {
    acc[cur] = [];
    reportCount[cur] = 0;
    return acc;
  }, {});

  report.map((reportId) => {
    const [key, value] = reportId.split(" ");
    if (user[key].includes(value)) return;

    user[key] = [...user[key], value];
    reportCount[value]++;
  });

  const pauseUser = Object.entries(reportCount)
    .map(([key, value]) => {
      if (value >= k) return key;
    })
    .filter((name) => name !== undefined);

  return Object.values(user)
    .map((reportList) => pauseUser.filter((user) => reportList.includes(user)))
    .map((arr) => arr.length);
}

solution(
  ["muzi", "frodo", "apeach", "neo"],
  ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
  2
);

solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3);
