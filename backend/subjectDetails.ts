export async function getStudents(client, user, sub) {

    let results = await client.query(
        `SELECT * FROM ?? WHERE FACULTY = ?`, [sub.replaceAll(" ","_"), user]
    );

    return {
        status: 200,
        data: {
            message: "Successful",
            subjects: results,
            sub: sub
        }
    }

}