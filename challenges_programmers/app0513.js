let routes = [{ name: "root", id: "" }];
const APIURL =
	"https://zl3m4qq0l9.execute-api.ap-northeast-2.amazonaws.com/dev";
let imageViewer = "";
let loadingModal = "";
let nodes = "";

const breadCrumb = (routeName) => {
	return `<div>${routeName}</div>`;
};

const Node = (id, name, filePath, type) => {
	return `
    <div class="Node ${type}" id="${id}" onclick="onClickElement(this)">
        <img src="${
			type == "DIRECTORY" ? "./assets/directory.png" : "./assets/file.png"
		}">
        <div>${name}</div>
        ${
			type === "FILE"
				? `<img class="imagePath" src="https://fe-dev-matching-2021-03-serverlessdeploymentbuck-t3kpj3way537.s3.ap-northeast-2.amazonaws.com/public${filePath}" style="visibility: hidden;"></img>`
				: ""
		}
        
    </div>
    `;
};

const backButton = () => {
	return `
    <div class="Node" onclick="onBackButtonClick()">
        <img src="./assets/prev.png">
    </div>
    `;
};

const onClickElement = (el) => {
	console.log(el);
	let id = el.id;
	if (el.classList.contains("DIRECTORY")) {
		fetchAndUpdate(id).then(() => {
			routes.push({
				name: el.innerText,
				id: el.id,
			});
			document.querySelector(".Breadcrumb").innerHTML = routes.reduce(
				(prev, cur) => {
					return prev + breadCrumb(cur.name);
				},
				""
			);
		});
	} else if (el.classList.contains("FILE")) {
		let path = el.querySelector(".imagePath").src;
		showImage(path);
	}
};

const onBackButtonClick = () => {
	routes.pop();
	fetchAndUpdate(routes[routes.length - 1].id);
};

const showImage = (path) => {
	let content = `<div class="content"><img src="${path}"></div>`;
	imageViewer.innerHTML = content;
	imageViewer.style.visibility = "visible";
};

const fetchAndUpdate = async (id) => {
	loadingModal.style.visibility = "visible";
	return await fetch(`${APIURL}/${id}`)
		.then((res) => {
			console.log(res.clone().json());
			return res.clone().json();
		})
		.then((data) => {
			let html = id === "" ? "" : backButton();
			nodes.innerHTML = data.reduce((prev, cur) => {
				console.log(cur);
				return prev + Node(cur.id, cur.name, cur.filePath, cur.type);
			}, html);
		})
		.catch((e) => [])
		.finally(() => (loadingModal.style.visibility = "hidden"));
};

window.onload = () => {
	imageViewer = document.querySelector(".ImageViewer");
	loadingModal = document.querySelector(".Loading");
	console.log(loadingModal);
	nodes = document.querySelector(".Nodes");

	imageViewer.addEventListener("click", (event) => {
		imageViewer.style.visibility = "hidden";
	});
	imageViewer.addEventListener("keydown", (event) => {
		if (event.key === "Escape") {
			imageViewer.style.visibility = "hidden";
		}
	});

	fetchAndUpdate("");
};
