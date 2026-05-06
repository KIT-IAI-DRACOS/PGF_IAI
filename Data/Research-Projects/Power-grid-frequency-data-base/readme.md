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

<label for="txtSearchStandaloneMetadata">Enter text to search the table</label>
<input type="input" id="txtSearchStandaloneMetadata" name="txtSearchStandaloneMetadata"/>
  <table id="metadataStandalone" style="width: 980px">
   <thead>
      <tr>
        <th>Location</th>
        <th>Country</th>
        <th>Resolution</th>
        <th>Date Range</th>
        <th>Path</th>
        <th>Analysis</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>



  <script>

    async function loadMetadata() {
      const response = await fetch("./../assets/files/iceland.json");
      const data = await response.json();

      const tbody = document.querySelector("#metadataStandalone tbody");
      tbody.innerHTML = "";

      locationValue=`<label>${data.spatial.location.address}</label>`;
      country=`<label>${data.spatial.extent.name}</label>`;
      temporal=`<label>${data.temporal.timeseries[0].resolutionValue}</label>`;
      dateRange=`<label>${data.temporal.timeseries[0].start}<br/>${data.temporal.timeseries[0].end}</label>`; 
      path=`<a href="${data.path}" target="_blank">OSF Link</a>`;
      analysis=`<button id="btnAnalysis" title="Analysis plot is from ${data.temporal.timeseries[0].start} to ${data.temporal.timeseries[0].end}" class="btnAnalysis" onclick="runAnalysis()">Analysis</button>`;

      row = document.createElement("tr"); 

      [row, locationValue, country, temporal, path];

      locationCell = document.createElement("td");
      locationCell.innerHTML = locationValue;

      countryCell = document.createElement("td");
      countryCell.innerHTML = country;

      temporalCell = document.createElement("td");
      temporalCell.innerHTML = temporal;

      dateRangeCell = document.createElement("td");
      dateRangeCell.innerHTML = dateRange;

      pathCell = document.createElement("td");
      pathCell.innerHTML = path;

      analysisCell = document.createElement("td");
      analysisCell.innerHTML = analysis;

      row.appendChild(locationCell);
      row.appendChild(countryCell);
      row.appendChild(temporalCell);
      row.appendChild(dateRangeCell);
      row.appendChild(pathCell);
      row.appendChild(analysisCell);

      tbody.appendChild(row);
    }

    loadMetadata();
    
    document.getElementById("txtSearchStandalone").onkeyup = e => {
        const rows = document.querySelectorAll("#dynamicStandalone tbody tr");
        for (const tr of rows)
            tr.style.display = tr.innerText.toLowerCase().includes(e.target.value.toLowerCase()) ? "" : "none";
    };

    document.getElementById("txtSearchStandaloneMetadata").onkeyup = e => {
        const rows = document.querySelectorAll("#metadataStandalone tbody tr");
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

  <style>
    .btnAnalysis {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 20px;
      background: linear-gradient(135deg, #f1c866, #f6c982);
      color: #fff;
      border: none;
      border-radius: 6px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      transition: opacity 0.2s, transform 0.1s;
    }
    .btnAnalysis:hover { opacity: 0.88; transform: translateY(-1px); }
    .btnAnalysis:active { transform: translateY(0); }
    .btnAnalysis:disabled { opacity: 0.55; cursor: not-allowed; transform: none; }
  </style>

  <br>
  <div id="divAnalysis" style="display:none;">
    <div id="plotAutocorr" style="width:100%; height:350px; margin-top:16px;"></div>
    <div id="plotHistogram" style="width:100%; height:350px; margin-top:16px;"></div>
  </div>

  <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
  <script>
    async function parseCSV(url) {
      const res = await fetch(url);
      const text = await res.text();
      const lines = text.trim().split('\n');
      const headers = lines[0].split(',').map(h => h.trim());
      const cols = {};
      headers.forEach(h => cols[h] = []);
      for (let i = 1; i < lines.length; i++) {
        const vals = lines[i].split(',');
        headers.forEach((h, j) => cols[h].push(parseFloat(vals[j])));
      }
      return { headers, cols };
    }

    async function runAnalysis() {
      const btn = document.getElementById('btnAnalysis');
      btn.disabled = true;
      btn.textContent = 'Loading...';

      const base = (typeof BASE_URL !== 'undefined') ? BASE_URL : '';
      const [autocorr, histogram] = await Promise.all([
        parseCSV('./../assets/files/IS01_autocorr.csv'),
        parseCSV('./../assets/files/IS01_histogram.csv')
      ]);

      document.getElementById('divAnalysis').style.display = 'block';

      const acH = autocorr.headers;
      Plotly.newPlot('plotAutocorr', [{
        x: autocorr.cols[acH[0]],
        y: autocorr.cols[acH[1]],
        type: 'scatter',
        mode: 'lines',
        line: { color: '#f19e63', width: 2 },
        name: acH[1]
      }], {
        title: { text: 'Autocorrelation', font: { size: 16 } },
        xaxis: { title: acH[0] },
        yaxis: { title: acH[1] },
        margin: { t: 50, r: 20, b: 50, l: 60 }
      }, { responsive: true });

      const hH = histogram.headers;
      Plotly.newPlot('plotHistogram', [{
        x: histogram.cols[hH[0]],
        y: histogram.cols[hH[1]],
        type: 'bar',
        marker: { color: '#f63bb5' },
        name: hH[1]
      }], {
        title: { text: 'Histogram', font: { size: 16 } },
        xaxis: { title: 'Frequency (Hz)' },
        yaxis: { title: 'Occurences' },
        margin: { t: 50, r: 20, b: 50, l: 60 }
      }, { responsive: true });

      btn.textContent = 'Analysis';
      btn.disabled = false;
    }
  </script>



The links are direct links to the `.csv` files from the Open Science Framework repository [Power grid frequency data base](https://osf.io/by5hu/).

**Licensing**: The authors request the associated [<a href="https://arxiv.org/abs/2006.01771" class="Blau">preprint</a>] be cited:
>*Power grid frequency data base*, R. Jumar, H. Maaß, B. Schäfer, L. Rydin Gorjão, V. Hagenmeyer, arXiv:2006.01771, 2020
