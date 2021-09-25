import puppeteer from "puppeteer";
var fs = require("fs");

var dir = "posters";

if (!fs.existsSync(dir)) {
	fs.mkdirSync(dir);
}

const doStuff = async () => {
	const iExistBecausePhilippeWantsIt = 5;
	const browser = await puppeteer.launch({
		defaultViewport: {
			width: 210 * iExistBecausePhilippeWantsIt,
			height: 297 * iExistBecausePhilippeWantsIt,
		},
	});
	for (let i = 1; i <= 75; i++) {
		const page = await browser.newPage();
		await page.goto("http://localhost:3000/ask/" + i, {
			waitUntil: "networkidle2",
		});
		const pdf = await page.screenshot({ path: `${dir}/screenshot${i}.png` });
		console.log("done", i);
	}
	await browser.close();
};

doStuff();
