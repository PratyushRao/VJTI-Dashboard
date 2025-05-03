export async function getSemData (client, branch, sem, rollno, semData) {

  for(let i = sem; i > 0; i--) {
    const results = await client.query(
      `SELECT SUBJECTS FROM Syllabus WHERE BRANCH = ? AND SEMESTER = ?`,
      [branch, i]
    );
    if (results.length > 0) {
      let subs =  results[0].SUBJECTS.split('|');
      for(let j of subs) {
        const subRes = await client.query(
          `SELECT GRADE, Attendance, FACULTY, CREDIT FROM ?? WHERE REG_NO = ?`,
          [j, rollno]
        );
        semData[i-1].push(subRes[0]);
      }
    }
  }

  if (semData.length > 0) {
    return {
      status: 200,
      data: {
        message: "Sem Data Found",
        isValid: true,
        semData: semData
      }
    }
  } else {
    return {
      status: 404,
      data: {
        message: "Sem Data Not Found",
        isValid: false
      }
    }
  }
}