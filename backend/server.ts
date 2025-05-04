import { serve } from "https://deno.land/std@0.224.0/http/server.ts";
import { Client } from "https://deno.land/x/mysql@v2.12.0/mod.ts";
import { validateUser } from "./loginAuth.ts";
import { getSemData } from "./semData.ts";
import { getStudents, addAtt, subAtt, changeGrade } from "./subjectDetails.ts";

//MySQL db connection
const client = await new Client().connect({
    hostname: "localhost",
    username: "root",
    db: "dti",
    password: "12345678"
});

getSemData(client, "EC", 2, "211090004", []).then((result) => {
    console.log(result);
}).catch((error) => {
    console.error("Error:", error);
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

    if (req.method === 'POST' && new URL(req.url).pathname === '/faculty') {
        try {
            const { user, sub } = await req.json();

            const studentList = await getStudents(client, user, sub);

            const headers = new Headers(corsHeaders);
            headers.set('Content-Type', 'application/json');

            //return authentication result
            return new Response(JSON.stringify(studentList.data), {
                headers,
                status: studentList.status
            });
        } catch (error) {
            const headers = new Headers(corsHeaders);
            headers.set('Content-Type', 'application/json');

            return new Response(JSON.stringify({
                message: "Failed to collect student's data",
                error: "Invalid Request"
            }), {
                headers,
                status: 500
            });
        }
    }


    if (req.method === 'POST' && new URL(req.url).pathname === '/addAttendance') {
        try {
            const {sub, reg, name } = await req.json();

            const Att = await addAtt(client, sub, reg, name);

            const headers = new Headers(corsHeaders);
            headers.set('Content-Type', 'application/json');

            //return authentication result
            return new Response(JSON.stringify(Att.data), {
                headers,
                status: Att.status
            });
        } catch (error) {
            const headers = new Headers(corsHeaders);
            headers.set('Content-Type', 'application/json');

            return new Response(JSON.stringify({
                message: "Failed to collect student's data",
                error: "Invalid Request"
            }), {
                headers,
                status: 500
            });
        }
    }

    if (req.method === 'POST' && new URL(req.url).pathname === '/subAttendance') {
        try {
            const {sub, reg, name } = await req.json();

            const Att = await subAtt(client, sub, reg, name);

            const headers = new Headers(corsHeaders);
            headers.set('Content-Type', 'application/json');

            //return authentication result
            return new Response(JSON.stringify(Att.data), {
                headers,
                status: Att.status
            });
        } catch (error) {
            const headers = new Headers(corsHeaders);
            headers.set('Content-Type', 'application/json');

            return new Response(JSON.stringify({
                message: "Failed to collect student's data",
                error: "Invalid Request"
            }), {
                headers,
                status: 500
            });
        }
    }
    if (req.method === 'POST' && new URL(req.url).pathname === '/changeGrade') {
        try {
            const {sub, reg, name, grade } = await req.json();

            const Gr = await changeGrade(client, sub, reg, name, grade);

            const headers = new Headers(corsHeaders);
            headers.set('Content-Type', 'application/json');

            return new Response(JSON.stringify(Gr.data), {
                headers,
                status: Gr.status
            });
        } catch (error) {
            const headers = new Headers(corsHeaders);
            headers.set('Content-Type', 'application/json');

            return new Response(JSON.stringify({
                message: "Failed to collect student's data",
                error: "Invalid Request"
            }), {
                headers,
                status: 500
            });
        }
    }
    if (req.method === 'POST' && new URL(req.url).pathname === '/semData') {
        try {
            const {sub, reg } = await req.json();

            const Att = await getStudents(client, sub, reg);

            const headers = new Headers(corsHeaders);
            headers.set('Content-Type', 'application/json');

            //return authentication result
            return new Response(JSON.stringify(Att.data), {
                headers,
                status: Att.status
            });
        } catch (error) {
            const headers = new Headers(corsHeaders);
            headers.set('Content-Type', 'application/json');

            return new Response(JSON.stringify({
                message: "Failed to collect student's data",
                error: "Invalid Request"
            }), {
                headers,
                status: 500
            });
        }
    }
    if( req.method === 'GET' && new URL(req.url).pathname === '/reports') {
        const { user, branch, sem, rollno } = await req.json();
        const semData = [];
    }

    // 404 Not Found
    return new Response(JSON.stringify({ message: "Not Found" }), {
        headers: new Headers(corsHeaders),
        status: 404
    });
};

serve(handler, { port: 8000 });