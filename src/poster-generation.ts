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
	const browserPano = await puppeteer.launch({
		defaultViewport: {
			width: 297 * iExistBecausePhilippeWantsIt,
			height: 210 * iExistBecausePhilippeWantsIt,
		},
	});
	for (let i = 1; i <= 75; i++) {
		const page = await browser.newPage();
		await page.goto("http://localhost:3000/poster/" + i, {
			waitUntil: "networkidle2",
		});
		const pdf = await page.screenshot({ path: `${dir}/screenshot${i}.png` });

		const pagePano = await browserPano.newPage();
		await pagePano.goto("http://localhost:3000/panorama/" + i, {
			waitUntil: "networkidle2",
		});
		const pdf2 = await pagePano.screenshot({
			path: `${dir}/screenshot${i}_pano.png`,
		});
		console.log("done", i);
	}
	await browser.close();
};

doStuff();
