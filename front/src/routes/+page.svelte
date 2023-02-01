<!-- <h1>Hello and welcome to my site!</h1>
<div>
    <button on:click={() => toDoList = func()}>
      toDoList 가져오기
    </button>
    
    <p>{text.}</p>
  </div>

<script>
    let toDoList = [];
    let text = "";
    async function func(){
        const url = 'http://127.0.0.1:5174/';
        const res = await fetch(url);
        text = res;

        console.log(text)
    }
</script>
  
<style> </style>
   -->
<script>
let test = "";
async function getTodos() {
    const url = 'http://127.0.0.1:5174/';

    const res = await fetch(url); // url로 비동기 요청에 대한 응답을 Promise 객체로 받습니다.

    let resData = await res.json();     // 응답받은 데이터를 json으로 변환

    if (res.ok) { // 정상적으로 응답받은 경우
    test = resData
    } else {
    throw new Error("error");
    }
}
</script>

<div>
<button on:click={() => getTodos()}>
    print
</button>
<p>{test}</p>
</div>