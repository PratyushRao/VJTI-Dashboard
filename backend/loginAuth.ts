import { serve } from "https://deno.land/std@0.224.0/http/server.ts";
import { Client } from "https://deno.land/x/mysql@v2.12.0/mod.ts";

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

const handler = async (req: Request) => {
    if (req.method === 'OPTIONS') {
        return new Response(null, {
            headers: new Headers(corsHeaders)
        });
    }
    if (req.method === 'POST' && new URL(req.url).pathname === '/login') {
        try {
            const { userType, username, password } = await req.json();


            if (userType === 'student') {
                const results = await client.query(
                    `SELECT * FROM students WHERE REG_NO = ? AND password = ?`,
                    [username, password]
                );
                const headers = new Headers(corsHeaders);
                headers.set('Content-Type', 'application/json');

                if (results.length > 0) {
                    return new Response(JSON.stringify({ message: "okay" }), {
                        headers,
                        status: 200
                    });
                } else {
                    return new Response(JSON.stringify({ message: "invalid" }), {
                        headers,
                        status: 401
                    });
                }
            }


            else if (userType === 'faculty') {
                const results = await client.query(
                    `SELECT * FROM faculty WHERE username = ? AND password = ?`,
                    [username, password]
                );
                const headers = new Headers(corsHeaders);
                headers.set('Content-Type', 'application/json');

                if (results.length > 0) {
                    return new Response(JSON.stringify({ message: "okay" }), {
                        headers,
                        status: 200
                    });
                } else {
                    return new Response(JSON.stringify({ message: "invalid" }), {
                        headers,
                        status: 401
                    });
                }
            }
        }

        catch (error) {
            const headers = new Headers(corsHeaders);
            headers.set('Content-Type', 'application/json');

            return new Response(JSON.stringify({ message: "invalid", error: error.message }), {
                headers,
                status: 500
            });
        }
    }

    // 404 for other routes
    return new Response(JSON.stringify({ message: "Not Found" }), {
        headers: new Headers(corsHeaders),
        status: 404
    });
};

console.log('Server running on http://localhost:8000');
serve(handler, { port: 8000 });