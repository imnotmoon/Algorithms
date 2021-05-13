const api_url =
	"https://zl3m4qq0l9.execute-api.ap-northeast-2.amazonaws.com/dev";
const photo_url =
	"https://fe-dev-matching-2021-03-serverlessdeploymentbuck-t3kpj3way537.s3.ap-northeast-2.amazonaws.com/public";
const nodes = document.getElementsByClassName("Nodes");
let breadCrumb = document.getElementsByClassName("Breadcrumb");
let routes = [{ name: "root", id: "" }];

const apiFetch = (nodeId) => {
	let url = api_url + "/" + nodeId;
	console.log(url);
	return fetch(url)
		.then((res) => {
			return res.clone().json();
		})
		.catch((e) => {
			console.log(e);
			return [];
		});
};

const onClickElement = (e) => {
	if (e.classList.contains("DIRECTORY")) {
		let id = e.id;
		console.log(`dir : ${id}`);
		routes.push({ name: e.innerText, id });
		let bc = routes.reduce((prev, cur) => {
			return prev + `<div>${cur.name}</div>`;
		}, "");
		breadCrumb[0].innerHTML = bc;
		loadItem(String(id));
	} else if (e.classList.contains("Prev")) {
		console.log("prev");
		routes.pop();
		let to = routes[routes.length - 1].id;
		let bc = routes.reduce((prev, cur) => {
			return prev + `<div>${cur.name}</div>`;
		}, "");
		breadCrumb[0].innerHTML = bc;
		loadItem(String(to));
	} else {
		console.log(e);
		console.log(e.querySelector("img"));
		let filePath = e.querySelector("img").src;
		console.log(`file : ${filePath}`);
		showPicture(filePath);
	}
};

const showPicture = (filePath) => {
	let component = `
        <div class="content">
        <img src="${filePath}">
    `;
	let content = document.querySelector(".Modal");
	content.innerHTML = component;
	content.style.visibility = "visible";
};

window.onload = async () => {
	let modal = document.querySelector(".Modal");
	console.log(modal);
	modal.addEventListener("keypress", (event) => {
		if (event.key == "Escape") {
			// 모달 켜기 / 끄기로 바꿔야할듯
			modal.style.visibility = "hidden";
		}
	});
	modal.addEventListener("click", (event) => {
		// 모달 끄기
		modal.style.visibility = "hidden";
	});
	let data = await apiFetch("").then((res) => {
		console.log(res);
		return res.reduce((pre, cur) => {
			let html =
				cur.type === "DIRECTORY"
					? `<div class="Node DIRECTORY" onclick="onClickElement(this)" id=${cur.id}>
                <img src="./assets/directory.png">
                <div>${cur.name}</div>
            </div>`
					: `<div class="Node FILE" onclick="onClickElement(this)" id=${cur.id}>
                안녕안녕
                <img src="${cur.filePath}">
                <div>${cur.name}</div>
            </div>`;
			return pre + html;
		}, "");
	});
	nodes[0].innerHTML = data;
};

const loadItem = async (dir) => {
	let data = await apiFetch(dir === "root" ? "" : dir).then((res) => {
		console.log(res);
		let pre = `<div class="Node Prev" onclick="onClickElement(this)">
            <img src="./assets/prev.png">
        </div>`;
		return res.reduce((pre, cur) => {
			let html =
				cur.type === "DIRECTORY"
					? `<div class="Node DIRECTORY" id="${cur.id}" onclick="onClickElement(this)">
                <img src="./assets/directory.png">
                <div>${cur.name}</div>
            </div>`
					: `<div class="Node FILE" id="${
							cur.id
					  }" onclick="onClickElement(this)">
                <img src="${photo_url + cur.filePath}">
                <div>${cur.name}</div>
            </div>`;
			return pre + html;
		}, pre);
	});
	nodes[0].innerHTML = data;
};

// 50분 남음
