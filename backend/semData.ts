export async function getSemData (client, branch, sem, rollno) {

  let semData: any = [];
  for(let i = 1; i <= sem; i++) {
    const results = await client.query(
      `SELECT SUBJECTS FROM Syllabus WHERE BRANCH = ? AND SEMESTER = ?`,
      [branch, i]
    );
    if (results.length === 0) {
      semData.push(`No subjects found for semester ${i}`);
    }
    if (results.length > 0) {
      let subs =  results[0].SUBJECTS.split('|');
      let subArr: object[] = []
      for(let j of subs) {
        const subRes = await client.query(
          `SELECT GRADE, Attendance, FACULTY, CREDIT FROM ?? WHERE REG_NO = ?`,
          [j, rollno]
        );
        subRes[0].SUBJECT = j.replaceAll("_", " ");
        subArr.push(subRes[0]);
      }
      semData.push(subArr)
    }
  }

  return semData;
}