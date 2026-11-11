import http from 'node:http';
import {readFile,stat} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=fileURLToPath(new URL('./dist/',import.meta.url));
const mime={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.jpg':'image/jpeg','.png':'image/png','.webp':'image/webp','.svg':'image/svg+xml'};
const port=Number(process.env.PORT||4173);
const server=http.createServer(async(req,res)=>{try{const url=new URL(req.url,'http://localhost');const decoded=decodeURIComponent(url.pathname);const relative=decoded==='/'?'index.html':decoded.replace(/^\/+/, '');const file=path.resolve(root,relative);if(!file.startsWith(root)||!(await stat(file)).isFile()){res.writeHead(404);res.end('Não encontrado');return;}const data=await readFile(file);res.writeHead(200,{'Content-Type':mime[path.extname(file)]||'application/octet-stream','Cache-Control':'no-cache','X-Content-Type-Options':'nosniff'});res.end(data);}catch{res.writeHead(404);res.end('Não encontrado');}});
server.listen(port,'127.0.0.1',()=>console.log(`Le Jardin: http://localhost:${port}`));
