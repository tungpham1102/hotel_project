function validateForm() {
  var first_name = document.forms["myForm"]["first_name"].value;
  var last_name = document.forms["myForm"]["last_name"].value;
  var birthday = document.forms["myForm"]["birthday"].value;
  var gender = document.forms["myForm"]["gender"].value;
  var phone = document.forms["myForm"]["phone"].value;
  if (first_name == "") {
    alert("First_name is required");
    return false;
  }
  else if (last_name == "") {
    alert("last name is required");
    return false;
  }
  else if (birthday == "") {
    alert("birthday must be filled out");
    return false;
  }
  else if (gender == "") {
    alert("gender must be filled out");
    return false;
  }
  else if (phone == "") {
    alert("phone must be filled out");
    return false;
  }
}