def Ecom():
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btChrome].Run("https://bearstore-testsite.smartbear.com/")
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'linkWatches' link.
    Aliases.browser.pageShop_new1.linkWatches.Click()
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageWatches.Wait()
    #Clicks the 'imageShowDetailsForCertinaDs' control.
    Aliases.browser.pageWatches.sectionContent.linkShowDetailsForCertinaDs.imageShowDetailsForCertinaDs.Click()
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageCertinaDsPodiumBigSize.Wait()
    #Clicks the 'linkAddToCart' link.
    Aliases.browser.pageCertinaDsPodiumBigSize.sectionContent.articleCertinaDsPodiumBigSize.asideCertinaDsPodiumBigSize.linkAddToCart.Click()
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageCertinaDsPodiumBigSize.Wait()
    #Clicks the 'textnode' control.
    Aliases.browser.pageCertinaDsPodiumBigSize.asideOffcanvasCart.linkRemove.textnode.Click()
    #Closes the 'BrowserWindow' window.
    Aliases.browser.BrowserWindow.Close()
    
