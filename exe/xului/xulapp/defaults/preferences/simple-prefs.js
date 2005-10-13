# Mozilla User Preferences

/* Do not edit this file.
 *
 * If you make changes to this file while the browser is running,
 * the changes will be overwritten when the browser exits.
 *
 * To make a manual change to preferences, you can visit the URL about:config
 * For more information, see http://www.mozilla.org/unix/customizing.html#prefs
 */

pref("security.checkloaduri", false);
pref("toolkit.defaultChromeURI", "chrome://simple/content/simple.xul");
/*
pref("general.useragent.extra.simple", "SimpleApp/0.1");
*/
pref("signed.applets.codebase_principal_support", true);
pref("intl.charsetmenu.browser.cache", "UTF-8");
pref("capability.principal.codebase.exeweb.id", "https://127.0.0.1:8081");
pref("capability.principal.codebase.exeweb.granted", "UniversalXPConnect");
pref("capability.principal.codebase.exessl.id", "https://127.0.0.1:8032");
pref("capability.principal.codebase.exessl.granted", "UniversalXPConnect");
pref("capability.principal.codebase.exefile.id", "chrome://simple");
pref("capability.principal.codebase.exefile.granted", "UniversalXPConnect");
