# EEGData
Guys please delete all of the rows that aren't EEG data. Here is some code that I wrote up for Google Apps Script:
function deleteRows() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var rows = sheet.getDataRange();
  var numRows = rows.getNumRows();
  var values = rows.getValues();

  var rowsDeleted = 0;
  for (var i = 0; i <= numRows - 1; i++) {
    var row = values[i];
    if (row[0] == 'delete' || row[1] == '') { // This searches all cells in columns A (change to row[1] for columns B and so on) and deletes row if cell is empty or has value 'delete'.
      sheet.deleteRow((parseInt(i)+1) - rowsDeleted);
      rowsDeleted++;
    }
  }
};
legit just copy and paste this into apps script and click 'new deployment', choose library, then click run. The session will end after 30 minutes so please click run every 30 minutes. 
