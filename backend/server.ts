import { serve } from "https://deno.land/std@0.224.0/http/server.ts";
import { Client } from "https://deno.land/x/mysql@v2.12.0/mod.ts";
import { validateUser } from "./loginAuth.ts";

//MySQL db connection
const client = await new Client().connect({
    hostname: "localhost",
    username: "root",
    db: "dti",
    password: "12345678",
});

const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
};

export const handler = async (req: Request): Promise<Response> => {
    //CORS preflight stuff
    if (req.method === 'OPTIONS') {
        return new Response(null, {
            headers: new Headers(corsHeaders)
        });
    }

    if (req.method === 'POST' && new URL(req.url).pathname === '/login') {
        try {
          const { userType, username, password } = await req.json()
            
            const authResult = await validateUser(client, userType, username, password);
            
            const headers = new Headers(corsHeaders);
            headers.set('Content-Type', 'application/json');
            
            //return authentication result
            return new Response(JSON.stringify(authResult.data), {
                headers,
                status: authResult.status
            });
        } catch (error) {
            const headers = new Headers(corsHeaders);
            headers.set('Content-Type', 'application/json');

            return new Response(JSON.stringify({ 
                message: "Login Failed", 
                error: "Check your password or username"
            }), {
                headers,
                status: 500
            });
        }
    }

    // 404 Not Found
    return new Response(JSON.stringify({ message: "Not Found" }), {
        headers: new Headers(corsHeaders),
        status: 404
    });
};

console.log('Server running on http://localhost:8000');
serve(handler, { port: 8000 });