async function getSubjectList(client, uname, pass) {
  const subjectList = await client.query(
    `SELECT SUBJECTS, NAME FROM faculty WHERE username = ? AND password = ?`,
    [uname, pass]
  );

  if (!subjectList.length) return {};

  const classes = await subjectList[0].SUBJECTS.split('|');
  const fUser = subjectList[0].NAME;
  const classData = {};
  console.log(classes);
  for (const clas of classes) {
    const subRes = await client.query(
      `SELECT * FROM ?? WHERE FACULTY = ?`,
      [clas, fUser]
    );

    if (subRes.length > 0) {
      const branch = subRes[0].BRANCH;
      const sem = subRes[0].SEM;
      classData[await clas.replaceAll("_", " ")] = [branch, sem];
    }
  }
  return classData;
}



export async function validateUser(client, utype, uname, pass) {
  let results;

  switch (utype) {
    case 'student':
      results = await client.query(
        `SELECT * FROM students WHERE REG_NO = ? AND password = ?`,
        [uname, pass]
      );
      break;
    case 'faculty':
      results = await client.query(
        `SELECT * FROM faculty WHERE username = ? AND password = ?`,
        [uname, pass]
      );
      break;
  }

  if (results.length > 0 && utype === 'student') return {
    status: 200,
    data: {
      message: "Login Successful",
      isValid: true,
      user: {
        name: results[0].NAME,
        roll: results[0].REG_NO || results[0].username,
        utype: utype
        //dob: results[0].DateOfBirth,
        //email: results[0].EmailAddress,
        //year: results[0].YEAR,
        //cgpa: results[0].CGPA
      }
    }
  }
  else if (results.length > 0 && utype === 'faculty') {

    const classData = await getSubjectList(client, uname, pass);

    return {
      status: 200,
      data: {
        message: "Login Successful",
        isValid: true,
        user: {
          name: results[0].NAME,
          utype: utype,
          classData: classData
        }
      }
    }
  }
  return {
    status: 401,
    data: {
      message: "Invalid Credentials :/",
      isValid: false
    }
  }
}