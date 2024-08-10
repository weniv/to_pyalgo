// 광고 변경 시, 아래 kgData만 변경하면 됩니다. 순서는 데이터 작성 순으로 적용됩니다.
const kgData = [
  {
    img: "./src/img/kg/inflearn-python10.webp",
    link: "https://inf.run/hCg5",
    content: "Python 알고리즘 베스트 10 강의",
  },
  {
    img: "./src/img/kg/weniv-world.png",
    link: "https://world.weniv.co.kr/",
    content: "파이썬 교육 플랫폼, 위니브 월드",
  },
  {
    img: "./src/img/kg/weniv-scholar.webp",
    link: "https://scholarship.weniv.co.kr/",
    content: "위니브 청년 ICT 부스트 장학금",
  },
  {
    img: "./src/img/kg/inflearn-bootcamp.webp",
    link: "https://inf.run/pAne",
    content: "파이썬 부트캠프",
  },
  {
    img: "./src/img/kg/inflearn-cote.webp",
    link: "https://inf.run/RCuz",
    content: "눈떠보니 코딩테스트 전날",
  },
];

const slideTime = 3000;

const $kg = document.querySelector(".kg-carousel");
const $kgList = document.querySelector(".kg-list");
const $prevBtn = document.querySelector(".prev-btn");
const $nextBtn = document.querySelector(".next-btn");
const $pageList = document.querySelector(".page-list");

// 초기화
let kgIndex = 0;
let kgLength = kgData.length;
kgData.forEach((kg, index) => {
  const $kgItem = document.createElement("li");
  $kgItem.classList.add("kg-item");
  $kgItem.innerHTML = `
        <a href="${kg.link}" target="_blank">
        <img src="${kg.img}" alt="${kg.content} 바로가기" />
        </a>
    `;
  $kgList.appendChild($kgItem);

  const pageItem = document.createElement("li");
  pageItem.classList.add("page-item");
  pageItem.innerHTML = `<span class="page-number sr-only">${index + 1}</span>`;
  $pageList.appendChild(pageItem);
  if (index === 0) {
    pageItem.classList.add("active");
  }
  pageItem.addEventListener("click", () => {
    const $active = document.querySelector(".page-item.active");
    $active.classList.remove("active");
    pageItem.classList.add("active");

    kgIndex = index;
    $kgList.style.transform = `translateX(-${kgIndex * 100}%)`;
  });
});

// 버튼 변경
function prevMove() {
  if (kgIndex === 0) {
    kgIndex = kgLength - 1;
  } else {
    kgIndex--;
  }
  $kgList.style.transform = `translateX(-${kgIndex * 100}%)`;
  const $active = document.querySelector(".page-item.active");
  $active.classList.remove("active");
  $pageList.children[kgIndex].classList.add("active");
  $kgList.style.transform = `translateX(-${kgIndex * 100}%)`;
}
$prevBtn.addEventListener("click", prevMove);

function nextMove() {
  if (kgIndex === kgLength - 1) {
    kgIndex = 0;
  } else {
    kgIndex++;
  }
  $kgList.style.transform = `translateX(-${kgIndex * 100}%)`;
  const $active = document.querySelector(".page-item.active");
  $active.classList.remove("active");
  $pageList.children[kgIndex].classList.add("active");
  $kgList.style.transform = `translateX(-${kgIndex * 100}%)`;
}
$nextBtn.addEventListener("click", nextMove);
// 페이지네이션 변경

// 자동 변경
let loopInterval = setInterval(() => {
  nextMove();
}, slideTime);

$kg.addEventListener("mouseover", () => {
  clearInterval(loopInterval);
});
$kg.addEventListener("mouseout", () => {
  loopInterval = setInterval(() => {
    nextMove();
  }, slideTime);
});
