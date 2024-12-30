def Login():
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btChrome].Run("https://bearstore-testsite.smartbear.com/")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'linkLogIn' link.
    Aliases.browser.pageBearstoreTestsiteSmartbearCo.header.navUsd.navMenubarMyAccount.linkLogIn.Click()
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageShop.Wait()
    #Clicks the 'textboxUsernameoremail' control.
    Aliases.browser.pageShop.sectionContent.textboxUsernameoremail.Click()
    #Sets the text 'djl' in the 'textboxUsernameoremail' text editor.
    Aliases.browser.pageShop.sectionContent.textboxUsernameoremail.SetText("djl")
    #Sets the text Project.Variables.Password1 in the 'passwordboxPassword' text editor.
    Aliases.browser.pageShop.sectionContent.passwordboxPassword.SetText(Project.Variables.Password1)
    #Clicks the 'buttonLogIn' button.
    Aliases.browser.pageShop.sectionContent.buttonLogIn.ClickButton()
    #Delays the test execution for the specified time period.
    Delay(1000)
    #Checks whether the 'contentText' property of the Aliases.browser.pageBearstoreTestsiteSmartbearCo.FindElement("//h1[.='Welcome to our store.']") object equals 'Welcome to our store.'.
    aqObject.CheckProperty(Aliases.browser.pageBearstoreTestsiteSmartbearCo.FindElement("//h1[.='Welcome to our store.']"), "contentText", cmpEqual, "Welcome to our store.")
