function submitData() {
  console.log("Hello")
  var data = {};

  var select_gender = document.getElementById("genderdropdown");
  var select_state = document.getElementById("statedropdown");
  var select_otcota = document.getElementById("otcotadropdown");
  var select_education = document.getElementById("educationdropdown");
  var select_location = document.getElementById("locationtypedropdown");
  var select_payrate = document.getElementById("payratedropdown");
  var select_yearsofedu = document.getElementById("yearsofeducationdropdown");

  data["gender"] = select_gender.value;
  data["state"] = select_state.value;
  data["otcota"] = select_otcota.value;
  data["education"] = select_education.value;
  data["location"] = select_location.value;
  data["payrate"] = select_payrate.value;
  data["yearsofedu"] = select_yearsofedu.value;

  console.log(data);
  Get("predict/"+encodeURIComponent(JSON.stringify(data)));

}

function Get(stringInput){
  // var stringInput = "aleccheckthisout";
  // var stringInput_Arr = JSON.stringify(array)
  var Httpreq = new XMLHttpRequest();
  var baseSiteURL = 'https://safe-harbor-54765.herokuapp.com/';
  var httpURL = baseSiteURL + stringInput;
  console.log(httpURL);
  Httpreq.open("GET",httpURL, true);
  Httpreq.send(null);
  console.log(Httpreq.responseText);
  location.href = httpURL;
  return Httpreq.responseText;
}
