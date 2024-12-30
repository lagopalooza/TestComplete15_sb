def SmartBank_Checking_form():
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btChrome].Run("http://smartbank.se.smartbear.io/")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    Project.Variables.Varloop.Reset()
    RecordIdx = 1
    while RecordIdx <= 10:
        #Clicks the 'textnode' control.
        Aliases.browser.pageHome.header.nav.textnodePersonal.textnode.Click()
        #Clicks the 'linkChecking' link.
        Aliases.browser.pageHome.header.nav.textnodeChecking.linkChecking.Click()
        #Waits until the browser loads the page and is ready to accept user input.
        Aliases.browser.pageHome2.Wait()
        #Clicks the 'textboxFirstName' control.
        Aliases.browser.pageHome2.textnodePersonalInformation.textboxFirstName.Click()
        #Sets the text KeywordTests.SmartBank_Checking_form.Variables.Varloop["FirstName"] in the 'textboxFirstName' text editor.
        Aliases.browser.pageHome2.textnodePersonalInformation.textboxFirstName.SetText(Project.Variables.Varloop.Value["FirstName"])
        #Sets the text KeywordTests.SmartBank_Checking_form.Variables.Varloop["LastName"] in the 'textboxLastName' text editor.
        Aliases.browser.pageHome2.textnodePersonalInformation.textboxLastName.SetText(Project.Variables.Varloop.Value["LastName"])
        #Enters KeywordTests.SmartBank_Checking_form.Variables.Varloop["DOB"] in the 'dateinputDateOfBirth' object.
        Aliases.browser.pageHome2.textnodePersonalInformation.dateinputDateOfBirth.Keys(Project.Variables.Varloop.Value["DOB"])
        #Sets the text KeywordTests.SmartBank_Checking_form.Variables.Varloop["Address"] in the 'textboxAddress1' text editor.
        Aliases.browser.pageHome2.textnodePersonalInformation.textboxAddress1.SetText(Project.Variables.Varloop.Value["Address"])
        #Sets the text KeywordTests.SmartBank_Checking_form.Variables.Varloop["City"] in the 'textboxCity' text editor.
        Aliases.browser.pageHome2.textnodePersonalInformation.textboxCity.SetText(Project.Variables.Varloop.Value["City"])
        #Sets the text KeywordTests.SmartBank_Checking_form.Variables.Varloop["State"] in the 'textboxState' text editor.
        Aliases.browser.pageHome2.textnodePersonalInformation.textboxState.SetText(Project.Variables.Varloop.Value["State"])
        #Sets the text KeywordTests.SmartBank_Checking_form.Variables.Varloop["Zip"] in the 'textboxZipCode' text editor.
        Aliases.browser.pageHome2.textnodePersonalInformation.textboxZipCode.SetText(Project.Variables.Varloop.Value["Zip"])
        #Sets the text KeywordTests.SmartBank_Checking_form.Variables.Varloop["Email"] in the 'emailinputEmailAddress' text editor.
        Aliases.browser.pageHome2.textnodePersonalInformation.emailinputEmailAddress.SetText(Project.Variables.Varloop.Value["Email"])
        #Sets the text KeywordTests.SmartBank_Checking_form.Variables.Varloop["Phone"] in the 'phoneinputPhoneNumber' text editor.
        Aliases.browser.pageHome2.textnodePersonalInformation.phoneinputPhoneNumber.SetText(Project.Variables.Varloop.Value["Phone"])
        #Sets the text KeywordTests.SmartBank_Checking_form.Variables.Varloop["Occupation"] in the 'phoneinputOccuptation' text editor.
        Aliases.browser.pageHome2.textnodePersonalInformation.phoneinputOccuptation.SetText(Project.Variables.Varloop.Value["Occupation"])
        #Clicks the 'buttonSubmit' button.
        Aliases.browser.pageHome2.textnodePersonalInformation.buttonSubmit.ClickButton()
        Project.Variables.Varloop.Next()
        RecordIdx = RecordIdx + 1
