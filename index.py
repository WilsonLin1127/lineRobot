if (event.message.text == ‘牛奶’) {
var options = { method: ‘GET’,
	url: ‘https://api.imgur.com/3/album/DhjD2qC/images',
	headers:

	{ ‘access-token’: ‘1aa38cf2b25911e7fb2a6ed35fc5a195de152799’,
	‘cache-control’: ‘no-cache’,
	 authorization: ‘Client-ID 33856f8e35e5df5’ } };
	 
request(options, function (error, response, body) {

if (error) throw new Error('***'+error);

request(options, function (error, response, body) {
if (error) throw new Error(error);

console.log(Math.floor(Math.random()*JSON.parse(body).data.length));
console.log(JSON.parse(body).data[Math.floor(Math.random()*JSON.parse(body).data.length)].id);

var url= “https://imgur.com/" + JSON.parse(body).data[Math.floor(Math.random()*JSON.parse(body).data.length)].id + ‘.jpg’
event.reply({
type: ‘image’,
originalContentUrl: url,
previewImageUrl: url
});
});
}
