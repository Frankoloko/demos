// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require('vscode');
const http = require('request');

// this method is called when your extension is activated
// your extension is activated the very first time the command is executed

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "francois sql test" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with  registerCommand
	// The commandId parameter must match the command field in package.json
	context.subscriptions.push(vscode.commands.registerCommand('myExtension.createNewConnection', async () => {
		// The code you place here will be executed every time your command is executed
		console.log('myExtension.createNewConnection');

		// HIER CODE EK
			try {
				let theErrorFound = null;

				// Get target list & Let the user pick the target he wants to connect to
					let targetList = null;
					await new Promise(resolve => {
						http.get('http://localhost:3700/dbTarget', (err, res, body) => {
							if (err) return resolve(theErrorFound = err);
							resolve(targetList = JSON.parse(body).data);
						});
					});
					if (theErrorFound) throw(theErrorFound);

					const targetDisplayList = targetList.map(element => element.id);
					const selectedTarget = await vscode.window.showQuickPick(targetDisplayList, {
						placeHolder: 'Select a target to connect to...'
						// onDidSelectItem: item => vscode.window.showInformationMessage(`Focus ${++i}: ${item}`)
					});

					const selectedTargetObject = targetList.filter(element => element.id == selectedTarget)[0];

				// Get record list & Let the user pick the record he wants to connect to
					let recordList = null;
					await new Promise(resolve => {
						http.post({headers: {'content-type': 'application/json'}, url: 'http://localhost:3700/utGetRecordList', body: JSON.stringify(selectedTargetObject)}, (err, res, body) => {    
							if (err) return resolve(theErrorFound = err);
							resolve(recordList = JSON.parse(body).data);
						});
					});
					if (theErrorFound) throw(theErrorFound);

					const recordDisplayList = recordList.map(element => `${element[selectedTargetObject.settings.descriptioncolumn]} \t\t (${element[selectedTargetObject.settings.pkcolumn]})`);
					const selectedRecord = await vscode.window.showQuickPick(recordDisplayList, {
						placeHolder: 'Select a record to connect to...'
						// onDidSelectItem: item => vscode.window.showInformationMessage(`Focus ${++i}: ${item}`)
					});

					const selectedRecordObject = recordList.filter(element => (`${element[selectedTargetObject.settings.descriptioncolumn]} \t\t (${element[selectedTargetObject.settings.pkcolumn]})`) == selectedRecord)[0];
					
				// Open the selected file
					async function openInUntitled(content, language) {
						const document = await vscode.workspace.openTextDocument({
							language,
							content,
						});
						vscode.window.showTextDocument(document);
					}

					if (selectedTargetObject.filetype.toLowerCase() == 'sql') {
						openInUntitled(selectedRecordObject[selectedTargetObject.settings.valuecolumn], 'sql');
					}

					if (selectedTargetObject.filetype.toLowerCase() == 'js' || selectedTargetObject.filetype.toLowerCase() == 'javascript' || selectedTargetObject.filetype.toLowerCase() == 'java script' || selectedTargetObject.filetype.toLowerCase() == 'jscript' || selectedTargetObject.filetype.toLowerCase() == 'j script') {
						addText = '// The extension uses the below data to push the file back to the database\n';
						addText += '\t// RECORD DESCRIPTION: ' + selectedRecordObject[selectedTargetObject.settings.descriptioncolumn] + '\n';
						addText += '\t// RECORD PK VALUE: ' + selectedRecordObject[selectedTargetObject.settings.pkcolumn] + '\n';
						addText += '\t// TARGET: ' + JSON.stringify(selectedTargetObject) + '\n';
						addText += '// #####\n\n';
						
						openInUntitled(addText + selectedRecordObject[selectedTargetObject.settings.valuecolumn], 'javascript');
					}
			} catch (err) {
				console.log(err);
				vscode.window.showErrorMessage(err);
			}
			
		// HIER CODE EK
	}));

	context.subscriptions.push(vscode.commands.registerCommand('myExtension.updateFile', async () => {
		// The code you place here will be executed every time your command is executed
		console.log('myExtension.updateFile');

		// HIER CODE EK
			try {
				// Get the active editor's text
					let activeEditor = vscode.window.activeTextEditor;
					if (!activeEditor) {
						vscode.window.showErrorMessage('No edit window is active');
						return;
					}
					let editorText = activeEditor.document.getText();

				// Ask the user for a version comment
					let versionComment = await vscode.window.showInputBox({
						placeHolder: 'Add a comment for this version...'
					});
					if (versionComment == undefined) versionComment = '';

				// Split the data comments from the rest of the file
					const cutPosition = editorText.indexOf('#####');
					const dataComments = editorText.slice(0, cutPosition + 5);
					const editorTextWithoutDataComments = editorText.slice(cutPosition + 7, editorText.length);

					const positionRecordPKValue = dataComments.indexOf('RECORD PK VALUE:');
					const positionTarget = dataComments.indexOf('TARGET:');
					const positionHashes = dataComments.indexOf('// #####');

					const pkValue = dataComments.slice(positionRecordPKValue + 17, positionTarget - 5);
					const target = dataComments.slice(positionTarget + 8, positionHashes - 1);

				// Send the data back to the database
					const postBody = {
						pkValue: pkValue,
						target: target,
						newValue: editorTextWithoutDataComments,
						comment: versionComment
					}

					await new Promise(resolve => {
						http.post({headers: {'content-type': 'application/json'}, url: 'http://localhost:3700/utUpdateRecord', body: JSON.stringify(postBody)}, (err, res, body) => {    
							if (err) return resolve(theErrorFound = err);
				
							body = JSON.parse(body);
							if (body.result == 'error') {
								return resolve(theErrorFound = JSON.stringify(body.data));
							} else {
								return resolve(vscode.window.showInformationMessage('Record successfully updated'));
							}
						});
					});
					if (theErrorFound) throw(theErrorFound);
			} catch (err) {
				console.log(err);
				vscode.window.showErrorMessage(err);
			}
		// HIER CODE EK
	}));
}

// this method is called when your extension is deactivated
function deactivate() {}

module.exports = {
	activate,
	deactivate
}
