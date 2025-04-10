<<<<<<< HEAD
// Only make Promise
function getResponseFromAPI() {
	return new Promise((resolve, reject) => {
		/* eslint-disable */
		if (true) {
			resolve();
		} else {
			reject();
		}
		/* eslint-enable */
	});
}

export default getResponseFromAPI;
=======
export default function getResponseFromAPI() {
	  return new Promise((resolve) => {
		      resolve('Success');
		    });
}
>>>>>>> 3d608e94 (kllkj)
