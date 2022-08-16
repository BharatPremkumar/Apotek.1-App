class Avvik {
  constructor(plukkdato, plukknr, lokasjon, feilType) {
    this.plukkdato = plukkdato;
    this.plukknr = plukknr;
    this.lokasjon = lokasjon;
    this.feilType = feilType;
  }
}

function registrerAvvik() {
  var avvik = new Avvik(
    String(document.getElementById("plukkdato").value),
    Number(document.getElementById("plukknr").value),
    String(document.getElementById("lokasjon").value),
    String(document.getElementById("feilType").value)
  );

  //console.log(avvik);

  var xhr = new XMLHttpRequest();
  var url = "/up";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      alert("Avviket ble registrert");
    }
  };
  xhr.send(JSON.stringify(avvik));
}

document.getElementById("registrerBtn").addEventListener("click", registrerAvvik);
