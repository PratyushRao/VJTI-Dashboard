export async function validateUser(client, utype, uname, pass) {
  let results;
  
  switch(utype){
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

  if (results.length > 0) return {
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
  return {
    status: 401,
    data: {
      message: "Invalid Credentials :/",
      isValid: false
    }
  }
}