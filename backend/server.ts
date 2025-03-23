// basic deno server. This is NOT the final version of the server. We'll need to change most of the shit here lol
// to run, first CD to ./backend and then "deno run --allow-net server.ts" in your terminal

import { serve } from "https://deno.land/std@0.177.0/http/server.ts";
const port = 8000;

//handler function for incoming requests
function handler(req: Request): Response {
  const url = new URL(req.url);
  const path = url.pathname;
  
  console.log(`${req.method} request to ${path}`);
  
  //routing
  switch (path) {
    case "/":
      return new Response("Welcome to the Deno HTTP Server!", 
        {status: 200, headers: { "Content-Type": "text/plain" }});
    break;
    case "/json":
      return new Response(
        JSON.stringify({ message: "This is JSON data", timestamp: new Date() }),
        { status: 200, headers: { "Content-Type": "application/json" }});
    break;
    case "/html":
      return new Response( `<!DOCTYPE html>
      <html>
        <head>
          <title>Deno HTTP Server</title>
        </head>
        <body>
          <h1>Hello from Deno!</h1>
          <p>This is an HTML response.</p>
        </body>
        </html>`, { status: 200, headers: { "Content-Type": "text/html" } });
    break;
    default:
      return new Response("404 Not Found", { status: 404, headers: { "Content-Type": "text/plain" }});
  }
}

console.log(`HTTP server running on http://localhost:${port}`);

//start the server
await serve(handler, { port });