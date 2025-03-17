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

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dynamic Table</title>
</head>
<body>
  <table id="dynamicStandalone" border="1">
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

  <script>
    const jsonData = [
      { "location": "Reykjavík", "country": "Iceland", "synchronousArea": "Icelandic Grid", "Resolution":"1 sec", "dateRange":" 2017-10-14 - 2017-10-20", "noOfDays":"5.6","link":"<a href='https://osf.io/sxph8/download'>OSF link</a>", "size":"15.4"},
     { "location": "Vestmanna", "country": "Faroe Islands", "synchronousArea": "Faroe Grid", "Resolution":"1 sec", "dateRange":"   2019-11-03 - 2019-11-10 ", "noOfDays":"6.5","link":"<a href=\"https://osf.io/a7h5b/download\">OSF link</a>", "size":"24.5"},
     { "location": "Las Palmas de Gran Canaria, Canary Islands", "country": "Spain", "synchronousArea": "Gran Canarian Grid", "Resolution":"1 sec", "dateRange":"   2018-02-04 - 2018-02-10 ", "noOfDays":"6.5","link":'<a href="https://osf.io/wz42b/download">OSF link</a>', "size":"16.2"}
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
</body>
</html>
| Location | Country | Synchronous Area | resolution |  date range | number of days | direct link | size (mb) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|  |  |  |  | |    | |  |
|  |  |  | 1 sec ||    |  |  |
|  |  | Gran Canarian Grid | 1 sec |  2018-02-04 - 2018-02-10 | 6.5  |  |  16.2 |
|   |    |    |    |  2018-11-25 - 2018-11-26 | 1.5   | [OSF link](https://osf.io/rukat/download) |  4.4 |
| Palma de Mallorca, Balearic Islands | Spain | Mallorcan Grid | 1 sec | 2019-09-29 - 2019-12-31 | 94.0  | [OSF link](https://osf.io/2qn9k/download) |  324 |
| London | United Kingdom | National Grid | 1 sec |  2019-03-04 - 2019-03-07 | 3.5  | [OSF link](https://osf.io/cfv47/download) | 9.2 |
|    |     |     |    |  2019-11-10 - 2019-12-31 | 51.1   | [OSF link](https://osf.io/h5ydu/download) | 135 |
| Lauris | France | Continental Europe | 1 sec |  2019-04-16 - 2019-04-27 | 12.0   | [OSF link](https://osf.io/hfsrz/download) | 41.2 |
| Split | Croatia | Continental Europe | 1 sec |  2019-04-09 - 2019-04-12 | 4.0  | [OSF link](https://osf.io/r9eh6/download) | 13.5 |
| Erice, Sicily | Italy | Continental Europe | 1 sec |  2019-07-02 - 2019-07-06 | 5.0  | [OSF link](https://osf.io/c754b/download) | 17.1 |
| Krakau | Poland | Continental Europe | 1 sec |  2019-04-04 - 2019-04-07 | 4.0  | [OSF link](https://osf.io/wq3te/download) | 13.6 |
| Tallinn | Estonia | Baltic Grid | 1 sec |  2019-03-25 - 2019-04-17 | 22.9  | [OSF link](https://osf.io/t5ske/download) | 79.0 |
| Stockholm | Sweden | Nordic Grid | 1 sec |  2019-05-06 - 2019-05-13 | 6.7   | [OSF link](https://osf.io/e2xfb/download) | 23.1 |
| Lisbon | Portugal | Continental Europe | 1 sec |  2018-02-14 - 2018-02-21 | 6.8   | [OSF link](https://osf.io/5zgwn/download) | 16.8 |
| Salt Lake City, Utah | USA | Western Interconnection | 1 sec |  2019-05-19 - 2019-05-25 | 6.4   | [OSF link](https://osf.io/8rp4v/download) | 16.5 |
| College Station, Texas | USA | Texas Interconnection | 1 sec |  2019-05-15 - 2019-05-16 | 1.4   | [OSF link](https://osf.io/t5wxz/download) | 3.7 |
|    |    |     |    |  2019-05-20 - 2019-05-23 | 3.7   | [OSF link](https://osf.io/zngy8/download) | 9.6 |
| Cape Town | South Africa | South African Grid | 1 sec | 2017-11-19 - 2017-11-28 | 9.5   | [OSF link](https://osf.io/gzk7d/download) | 27.0 |
| St. Petersburg | Russia | Russian Grid | 1 sec |  2019-04-30 - 2019-05-12 | 13.0  | [OSF link](https://osf.io/tvsyc/download) | 44.5 |


The links are direct links to the `.csv` files from the Open Science Framework repository [Power grid frequency data base](https://osf.io/by5hu/).

**Licensing**: The authors request the associated [<a href="https://arxiv.org/abs/2006.01771" class="Blau">preprint</a>] be cited:
>*Power grid frequency data base*, R. Jumar, H. Maaß, B. Schäfer, L. Rydin Gorjão, V. Hagenmeyer, arXiv:2006.01771, 2020
