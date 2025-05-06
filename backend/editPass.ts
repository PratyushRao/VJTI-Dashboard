export async function editPassword(client,utype, uname, email, password){
    switch (utype) {
        case 'student':
          await client.query(
            `UPDATE STUDENTS SET PASSWORD= ? WHERE REG_NO = ? AND emailAddress = ?`,
            [password, uname, email]
          );
          break;
        case 'faculty':
            await client.query(
            `UPDATE FACULTY SET PASSWORD= ? WHERE USERNAME = ? AND EmailAddress = ?`,
            [password, uname, email]
          );
          break;
      }


      if (utype === 'student') return {
        status: 200,
        data: {
          message: "Student Password Updated",
          isValid: true,
          user: {
            regno:uname,
            email: email,
            utype: utype
          }
        }
      }
      else if (utype === 'faculty') {
        return {
          status: 200,
          data: {
            message: "Faculty Password Changed",
            isValid: true,
            user: {
                uname:uname,
                email: email,
                utype: utype
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