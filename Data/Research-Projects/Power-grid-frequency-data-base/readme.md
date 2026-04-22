This is a set of 19 recordings in 12 synchronous regions, spanning from 1 day to ~1 month in length, over 2017 to 2019, stored in the Open Science Framework [Power grid frequency data base](https://osf.io/by5hu/) since 2020.

### GPS-Synchronised measurements

Single link with the four recordings: [OSF link](https://osf.io/p5xyr/download) - 218 mb.

| Location | Country | Synchronous Area | resolution |  date range | number of days |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Karlsruhe | Germany | Continental Europe | 1 sec | 2019-07-09 - 2019-08-18 | 41.0 |
| Oldenburg | Germany | Continental Europe | 1 sec | 2019-07-10 - 2019-08-07 | 41.0 |
| Istanbul | Turkey |  Continental Europe  | 1 sec | 2019-07-09 - 2019-08-18 | 41.0 |
| Lisbon | Portugal |  Continental Europe  | 1 sec | 2019-07-09 - 2019-08-16 | 41.0 |


### Standalone measurements

<label for="txtSearchStandalone">Enter text to search the table</label>
<input type="input" id="txtSearchStandalone" name="txtSearchStandalone"/>
  <table id="dynamicStandalone" style="width: 980px">
    <thead>
      <tr>
        <th>Location</th>
        <th>Country</th>
        <th>Synchronous Area</th>
        <th>resolution</th>
        <th>date range</th>
        <th>number of days</th>
        <th>direct link</th>
        <th>size (mb)</th>
      </tr>
    </thead>
    <tbody>
    </tbody>
  </table>

  <table id="metadataStandalone" style="width: 980px">
   <thead>
      <tr>
        <th>Location</th>
        <th>Country</th>
        <th>Resolution</th>
        <th>Date Range</th>
        <th>Path</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>

<label id="output">Json text</label>

  <script>

    async function loadMetadata() {
      const response = await fetch("./assets/files/iceland.json");
      const data = await response.json();

      const tbody = document.querySelector("#metadataStandalone tbody");
      tbody.innerHTML = "";

      location=data.spatial.location.address;
      country=data.spatial.extent.name;
      temporal=`${data.temporal.timeseries[0].resolutionValue}${data.temporal.timeseries[0].resolutionUnit}`;
      dateRange=`${data.temporal.timeseries[0].start}-${data.temporal.timeseries[0].end}`;
      path=`<a href="${data.path}" target="_blank">OSF Link</a>`;

      const row = document.createElement("tr");

      [row, location, country, temporal, path];

      const locationCell = document.createElement("td");
      locationCell.innerHTML = location;

      const countryCell = document.createElement("td");
      countryCell.innerHTML = country;

      const temporalCell = document.createElement("td");
      temporalCell.innerHTML = temporal;

      const pathCell = document.createElement("td");
      pathCell.innerHTML = path;

      row.appendChild(locationCell);
      row.appendChild(countryCell);
      row.appendChild(temporalCell);
      row.appendChild(pathCell);

      tbody.appendChild(row);
    }

    populateTable();
    // fetch("./assets/files/iceland.json")
    //   .then(res => res.text())
    //   .then(text => {
    //     document.getElementById("output").textContent = text;
    // });
    
    document.getElementById("txtSearchStandalone").onkeyup = e => {
        const rows = document.querySelectorAll("#dynamicStandalone tbody tr");
        for (const tr of rows)
            tr.style.display = tr.innerText.toLowerCase().includes(e.target.value.toLowerCase()) ? "" : "none";
    };


    const jsonData = [
      { "location": "Reykjavík", "country": "Iceland", "synchronousArea": "Icelandic Grid", "Resolution":"1 sec", "dateRange":" 2017-10-14 - 2017-10-20", "noOfDays":"5.6","link":"<a href='https://osf.io/sxph8/download'>OSF link</a>", "size":"15.4"},
     { "location": "Vestmanna", "country": "Faroe Islands", "synchronousArea": "Faroe Grid", "Resolution":"1 sec", "dateRange":"   2019-11-03 - 2019-11-10 ", "noOfDays":"6.5","link":"<a href=\"https://osf.io/a7h5b/download\">OSF link</a>", "size":"24.5"},
     { "location": "Las Palmas de Gran Canaria, Canary Islands", "country": "Spain", "synchronousArea": "Gran Canarian Grid", "Resolution":"1 sec", "dateRange":"   2018-02-04 - 2018-02-10 ", "noOfDays":"6.5","link":'<a href="https://osf.io/wz42b/download">OSF link</a>', "size":"16.2"},
     { "location": "Las Palmas de Gran Canaria, Canary Islands", "country": "Spain", "synchronousArea": "Gran Canarian Grid", "Resolution":"1 sec", "dateRange":"   2018-11-25 - 2018-11-26 ", "noOfDays":"1.5","link":'<a href="https://osf.io/rukat/download">OSF link</a>', "size":"4.4"},
     { "location": "Palma de Mallorca, Balearic Islands", "country": "Spain", "synchronousArea": "Mallorcan Grid", "Resolution":"1 sec", "dateRange":"   2019-09-29 - 2019-12-31 ", "noOfDays":"94.0","link":'<a href="https://osf.io/2qn9k/download">OSF link</a>', "size":"324"},
     { "location": "London", "country": "United Kingdom", "synchronousArea": "National Grid", "Resolution":"1 sec", "dateRange":"   2019-03-04 - 2019-03-07 ", "noOfDays":"3.5","link":'<a href="https://osf.io/cfv47/download">OSF link</a>', "size":"9.2"},
     { "location": "London", "country": "United Kingdom", "synchronousArea": "National Grid", "Resolution":"1 sec", "dateRange":"   2019-11-10 - 2019-12-31 ", "noOfDays":"51.1","link":'<a href="https://osf.io/h5ydu/download">OSF link</a>', "size":"135"},
     { "location": "Lauris", "country": "France", "synchronousArea": "Continental Europe", "Resolution":"1 sec", "dateRange":"   2019-04-16 - 2019-04-27 ", "noOfDays":" 12.0 ","link":'<a href="https://osf.io/hfsrz/download">OSF link</a>', "size":"41.2"},
     { "location": "Split", "country": "Croatia", "synchronousArea": "Continental Europe", "Resolution":"1 sec", "dateRange":"   2019-04-09 - 2019-04-12 ", "noOfDays":" 4.0 ","link":'<a href="https://osf.io/r9eh6/download">OSF link</a>', "size":"13.5"},
     { "location": "Erice, Sicily", "country": "Italy", "synchronousArea": "Continental Europe", "Resolution":"1 sec", "dateRange":"   2019-07-02 - 2019-07-06 ", "noOfDays":" 5.0 ","link":'<a href="https://osf.io/c754b/download">OSF link</a>', "size":"17.1"},
    { "location": "Krakau", "country": "Poland", "synchronousArea": "Continental Europe", "Resolution":"1 sec", "dateRange":"   2019-04-04 - 2019-04-07 ", "noOfDays":" 4.0 ","link":'<a href="https://osf.io/wq3te/download">OSF link</a>', "size":"13.6"},
    { "location": "Tallinn", "country": "Estonia", "synchronousArea": "Baltic Grid", "Resolution":"1 sec", "dateRange":"   2019-03-25 - 2019-04-17 ", "noOfDays":" 22.9 ","link":'<a href="https://osf.io/t5ske/download">OSF link</a>', "size":"79.0"},
    { "location": "Stockholm", "country": "Sweden", "synchronousArea": "Nordic Grid", "Resolution":"1 sec", "dateRange":"   2019-05-06 - 2019-05-13 ", "noOfDays":" 6.5 ","link":'<a href="https://osf.io/e2xfb/download">OSF link</a>', "size":"23.1"},
    { "location": "Lisbon", "country": "Portugal", "synchronousArea": "Continental Europe", "Resolution":"1 sec", "dateRange":"   2018-02-14 - 2018-02-21 ", "noOfDays":" 6.8 ","link":'<a href="https://osf.io/5zgwn/download">OSF link</a>', "size":"16.8"},
    { "location": "Salt Lake City, Utah", "country": "USA", "synchronousArea": "Western Interconnection", "Resolution":"1 sec", "dateRange":"   2019-05-19 - 2019-05-25 ", "noOfDays":" 6.4 ","link":'<a href="https://osf.io/8rp4v/download">OSF link</a>', "size":"16.5"},
    { "location": "College Station, Texas", "country": "USA", "synchronousArea": "Texas Interconnection", "Resolution":"1 sec", "dateRange":"   2019-05-15 - 2019-05-16 ", "noOfDays":" 1.4 ","link":'<a href="https://osf.io/t5wxz/download">OSF link</a>', "size":"3.7"},
    { "location": "College Station, Texas", "country": "USA", "synchronousArea": "Texas Interconnection", "Resolution":"1 sec", "dateRange":"   2019-05-20 - 2019-05-23 ", "noOfDays":" 3.7 ","link":'<a href="https://osf.io/zngy8/download">OSF link</a>', "size":"9.6"},
    { "location": "Cape Town", "country": "South Africa ", "synchronousArea": "South African Grid", "Resolution":"1 sec", "dateRange":"   2017-11-19 - 2017-11-28 ", "noOfDays":" 9.5 ","link":'<a href="https://osf.io/gzk7d/download">OSF link</a>', "size":"27.0"},
    { "location": "St. Petersburg", "country": "Russia", "synchronousArea": "Russian Grid", "Resolution":"1 sec", "dateRange":"   2019-04-30 - 2019-05-12 ", "noOfDays":" 13.0 ","link":'<a href="https://osf.io/tvsyc/download">OSF link</a>', "size":"44.5"}
    ];

    const tableBody = document.getElementById('dynamicStandalone').getElementsByTagName('tbody')[0];

    jsonData.forEach(item => {
      let row = tableBody.insertRow();
      Object.values(item).forEach(text => {
        let cell = row.insertCell();
        if (text.includes("<a ")) {
            cell.innerHTML = text;
            } else {
            cell.textContent = text;
        }
      });
    });
  </script>



The links are direct links to the `.csv` files from the Open Science Framework repository [Power grid frequency data base](https://osf.io/by5hu/).

**Licensing**: The authors request the associated [<a href="https://arxiv.org/abs/2006.01771" class="Blau">preprint</a>] be cited:
>*Power grid frequency data base*, R. Jumar, H. Maaß, B. Schäfer, L. Rydin Gorjão, V. Hagenmeyer, arXiv:2006.01771, 2020
