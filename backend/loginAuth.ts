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
    data: {message: "okay"}
  }
  return {
    status: 401,
    data: {message: "Invalid Credentials :/"}
  }
}