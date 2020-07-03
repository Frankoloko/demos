function Car(pMake, pColor, pPlate) {
    this.Make = pMake;
    this.Color = pColor;
    this.Plate = pPlate;
    this.LogData = function () {
        console.log(this.Make + ' + ' + this.Color + ' + ' + this.Plate);
    }
}

function Car2(pValue) {
    if (pValue.hasOwnProperty ("TyreSize")) console.log ("has TyreSize as property");
    this.Make = pValue.Make;
    this.Color = pValue.Color;
    this.Plate = pValue.Plate;
    this.LogData = function () {
        console.log(this.Make + ' + ' + this.Color + ' + ' + this.Plate);
    }
}

var pars = {Make:"Jazz", Color:"White", Plate: "WDX 578 GP", TyreSize1:"17inc"};
FrancoisJazz2 = new Car2 (pars);

FrancoisJazz = new Car('Jazz', 'White', 'WDX 578 GP');
VironPolo = new Car('Polo', 'Groen', 'HPS 502 GP');
ThysKia = new Car('Kia', 'White', 'PSJ 935 GP');

FrancoisJazz.LogData();
VironPolo.LogData();
ThysKia.LogData();