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

export async function addAtt(client, sub, reg, name){
    await client.query(
        `UPDATE ?? SET Attendance = Attendance+1 WHERE REG_NO=? AND NAME=?`, [sub.replaceAll(" ","_"), reg, name]
    );
    let Att = await client.query(
        `SELECT Attendance FROM ?? WHERE REG_NO=? AND NAME=?`, [sub.replaceAll(" ","_"), reg,name]
    )
    const att= Att[0].Attendance;
    return {
        status: 200,
        data: {
            message: "Successful",
            Attendance: att
        }
    }
}

export async function subAtt(client, sub, reg, name){
    await client.query(
        `UPDATE ?? SET Attendance = Attendance-1 WHERE REG_NO=? AND NAME=?`, [sub.replaceAll(" ","_"), reg, name]
    );
    let Att = await client.query(
        `SELECT Attendance FROM ?? WHERE REG_NO=? AND NAME=?`, [sub.replaceAll(" ","_"), reg,name]
    )
    const att= Att[0].Attendance;
    return {
        status: 200,
        data: {
            message: "Successful",
            Attendance: att
        }
    }
}