import { totp } from 'D:/IIITD/dps_task/node_modules/hotp-totp-generator/index.js';

const totpToken = totp({ key: 'siddharth18313@iiitd.ac.inDPSCHALLENGE', X: 120 , T0: 0, algorithm: 'sha512'});
console.log(totpToken);
console.log(hotpOtpGenerator);