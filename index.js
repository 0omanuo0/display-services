const { app, BrowserWindow } = require('electron')

app.disableHardwareAcceleration() // Deshabilita la aceleración por hardware

// const a = fetch('http://127.0.0.1:5000/status');
// // print the json
// a.then((response) => {
//   return response.json();
// }).then((data) => {

//   // show only 2 decimal places
//   const memoryInMB = data.data[0].mem / 1024
//   const cpu = data.data[0].cpu
//   console.log(`CPU: ${cpu}%`)
//   console.log(`Memory: ${memoryInMB} MB`)
//   console.log(`CPU: ${parseFloat(cpu).toFixed(2)}%`)
//   console.log(`Memory: ${parseFloat(memoryInMB).toFixed(2)} MB`)
// });


function createWindow () {
  const win = new BrowserWindow({
    width: 480,
    height: 320,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    },
    autoHideMenuBar: true, // Ocultar la barra de menú
  })

  win.loadFile('index.html')
}

app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
