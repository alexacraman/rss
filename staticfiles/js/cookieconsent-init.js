
const cks =  Object.fromEntries(document.cookie.split('; ').map(v=>v.split(/=(.*)/s).map(decodeURIComponent)))


// const mapIT = new Map(document.cookie.split('; ').map(v=>v.split(/=(.*)/s).map(decodeURIComponent)))
// mapIT.forEach((el)=>{
//     console.log(el)//get the values
// })

// var manager = iframemanager();
// obtain cookieconsent plugin
var cc = initCookieConsent();

// microsoft logo
var logo = ''
var cookie = '';

// run plugin with config object
cc.run({
    current_lang : 'en',
    autoclear_cookies : true,                   // default: false,  Enable if you want to automatically delete cookies when user opts-out of a specific category inside cookie settings
    cookie_name: 'cc_cookie',             // default: 'cc_cookie'
    cookie_expiration : 365,                    // default: 182
    page_scripts: true,                         // default: false, Enable if you want to easily manage existing <script> tags.

    // auto_language: null,                     // default: null; could also be 'browser' or 'document'
    autorun: true,                           // default: true, If enabled, show the cookie consent as soon as possible (otherwise you need to manually call the .show() method)
    delay: 0,                                // default: 0
    force_consent: false,                   // Enable if you want to block page navigation until user action 
    hide_from_bots: false,                   // default: false, Enable if you don't want the plugin to run when a bot/crawler/webdriver is detected
    remove_cookie_tables:false  ,           // default: false, Enable if you want to remove the html cookie tables (but still want to make use of autoclear_cookies)
    cookie_domain: location.hostname,        // default: current domain
    cookie_path: "/",                        // default: root
    cookie_same_site: "Lax",
    use_rfc_cookie: false,                   // default: false
    // revision: 0,                             // default: 0

    gui_options: {
        consent_modal: {
            layout: 'bar',                      // box,cloud,bar
            position: 'bottom center',           // bottom,middle,top + left,right,center
            transition: 'slide'                 // zoom,slide
        },
        settings_modal: {
            layout: 'bar',                      // box,bar
            // position: 'left',                // right,left (available only if bar layout selected)
            transition: 'slide'                 // zoom,slide
        }
    },

    onFirstAction: function(user_preferences, cookie){
        // cc.showSettings(user_preferences, cookie)
        // callback triggered only once on the first accept/reject action
    },

    onAccept: function (cookie) {
        // cc.eraseCookies(['ad_privacy', 'ad_id'],['.amazon-adsystem.com'])
        // callback triggered on the first accept/reject action, and after each page load
    },

    onChange: function (cookie, changed_categories) {
        window.location.reload()
        // cc.run(changed_categories, cookie)
        // callback triggered when user changes preferences after consent has already been given
    },
    languages: {
        'en': {
            consent_modal: {
                title: cookie + ' We use cookies! ',
                description: 'This website uses essential cookies to ensure its proper operation and tracking cookies to understand how you interact with it. The latter will be set only after consent. <button type="button" data-cc="c-settings" class="cc-link">Manage Settings</button>',
                primary_btn: {
                    text: 'Accept all',
                    role: 'accept_all'              // 'accept_selected' or 'accept_all'
                },
                secondary_btn: {
                    text: 'Reject all',
                    role: 'accept_necessary'        // 'settings' or 'accept_necessary'
                }
            },
            settings_modal: {
                title: logo,
                save_settings_btn: 'Save settings',
                accept_all_btn: 'Accept all',
                reject_all_btn: 'Reject all',
                close_btn_label: 'Close',
                cookie_table_headers: [
                    {col1: 'Name'},
                    {col2: 'Domain'},
                    {col3: 'Expiration'},
                    {col4: 'Description'}
                ],
                blocks: [
                    {
                        title: 'Cookie usage',
                        description: 'I use cookies to ensure the basic functionalities of the website and to enhance your online experience. You can choose for each category to opt-in/out whenever you want. For more details relative to cookies and other sensitive data, please read the full <a href="https://www.redsleeves.co.uk/policy/" class="cc-link">privacy policy</a>.'
                    }, {
                        title: 'Strictly necessary cookies',
                        description: 'These cookies are essential for the proper functioning of my website. Without these cookies, the website would not work properly',
                        toggle: {
                            value: 'necessary',
                            enabled: true,
                            readonly: true          // cookie categories with readonly=true are all treated as "necessary cookies"
                        },
                        cookie_table_local: [
                            {
                            Name: 'cc_cookie',
                            Domain: location.hostname,
                            Expiration: '',
                            },
                            {
                                Name: 'csrftoken',
                                Domain: location.hostname,
                                Expiration: '',
                            }
                        ]
                    }, {
                        title: 'Performance and Analytics cookies',
                        description: 'These cookies allow the website to remember the choices you have made in the past',
                        toggle: {
                            value: 'analytics',     // there are no default categories => you specify them
                            enabled: true,
                            readonly: false
                        },
                        cookie_table: [
                            {
                                col1: '^_ga',
                                col2: 'google.com',
                                col3: '2 years',
                                col4: 'description ...',
                                is_regex: true
                            },
                            {
                                col1: '_gid',
                                col2: 'google.com',
                                col3: '1 day',
                                col4: 'description ...',
                            }
                        ]
                    }, {
                        title: 'Advertisement and Targeting cookies',
                        description: 'These cookies collect information about how you use the website, which pages you visited and which links you clicked on. All of the data is anonymized and cannot be used to identify you',
                        toggle: {
                            value: 'targeting',
                            enabled: true,
                            readonly: false
                        },
                        cookie_table: [
                            {
                                col1: 'IDE',
                                col2: 'doubleclick.net',
                                // col3: '2023-12-03T15:17:45.224Z',
                                
                            },
                            {
                                col1: '__Secure-3PSIDCC',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: '__Secure-1PSIDCC',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: 'SIDCC',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: '__Secure-3PAPISID',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: 'SAPISID',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: 'APISID',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: 'SSID',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: '__Secure-1PAPISID',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: 'HSID',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: '__Secure-3PSID',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: '__Secure-1PSID',
                                col2: '.google.co.uk',
                                
                            },
                            {
                                col1: 'SID',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: 'NID',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: 'OTZ',
                                col2: 'www.google.com',
                                
                            },
                            {
                                col1: 'SIDCC',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: '1P_JAR',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: 'AEC',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: 'SEARCH_SAMESITE',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: '__Secure-ENID',
                                col2: '.google.com',
                                
                            },
                            {
                                col1: 'ad-privacy',
                                col2: '.amazon-adsystem.com',
                                col3: '2023-12-12T20:10:44.246Z',
                                
                            }, {
                                col1: 'ad-id',
                                col2: '.amazon-adsystem.com',
                                col3: '2023-07-01T20:24:22.848Z',
                                
                            }
                        ]
                    }, {
                        title: 'More information',
                        description: 'For any queries in relation to my policy on cookies and your choices, please <a class="cc-link" href="https://www.redsleeves.co.uk/contact/">contact me</a>.',
                    }
                ]
            }
        }
    }

});




var local_column_key = [] 
cookieStore.getAll().then(cookies=>{
    cookies.forEach((el)=>{
        local_column_key.push({
                    Name: el.name,
                    Domain: location.hostname,
                    Expiration: el.expires,
                })
    })
})


var _log = function(print_msg){
    return console.log(print_msg)
 }
//  _log(local_column_key)

function getCookie (name) {
	let value = '; ' + document.cookie;
	let parts = value.split(`; ${name}=`);
	if (parts.length == 2) return parts.pop().split(';').shift();
}