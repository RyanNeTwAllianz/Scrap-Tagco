from utils.GetContainers import get_containers
from utils.GetTags import get_tags
from utils.CreateJson import create_json
from utils.ReadJson import read_json
from utils.ReduceTags import reduce_tags
from utils.ConvertToCsv import convert_to_csv
from utils.GuessX1Time import guess_x1_time

def test () -> None:
    #containers = read_json('containers')
    #tags = read_json('tags')
    #x = reduce_tags(tags, containers)
    #convert_to_csv(x)
    #print(x)
    x = guess_x1_time("""<script type="text/javascript"> 
//ga optout
tlz._disableGA = function() {
    window['ga-disable-UA-33617477-8'] = !0;
  	window['ga-disable-UA-33617477-20'] = !0;
    tlz._isGADisabled = !0;
    tlz.warn('GA is disabled');
};
if (tlz.cookie.get('disable-ga')) {
    tlz._disableGA();
}
//debug
if (tlz.getUrlParam('fullga')) {
    tlz.js('//www.google-analytics.com/analytics_debug.js');
}
//ids GA
tlz._alzGaID = 'UA-33617477-8';
tlz._alzExemptedGaID = 'UA-33617477-20';
tlz._getConsentGaIds = function(){
  return tlz.isOptin('analytics') ? [tlz._alzGaID, tlz._alzExemptedGaID] : tlz._alzExemptedGaID;
}
//consent mode
tlz._setConsentMode = function(mode){
  tlz.gt('consent', mode || 'default', {
    ad_storage: tlz.isOptin('ads') ? 'granted' : 'denied', 
    analytics_storage: 'granted'
  });
  tlz.gt('set', 'ads_data_redaction', tlz.isOptin('ads') ? false : true);
}
tlz._setConsentMode();
tlz.x1('listen saveOptin consent update', function(){
  tlz.evt.on('saveOptin', function(){ 
    tlz._setConsentMode('update');
  });
});
//init exempted
tlz.x1('init exempt - create ga tracker', function(){
  tlz.gt('config', tlz._alzExemptedGaID, { 
        groups: 'ga_exempt', 
        cookie_prefix: 'exempt',
        cookie_expires: 396 * 24 * 60 * 60, cookie_update: false, anonymize_ip: true, 
        allow_google_signals: false,
        allow_ad_personalization_signals: false,
        send_page_view: false,
        site_speed_sample_rate: 10, 
        cookie_flags: tlz._cookieSameSite ? 'SameSite=None; Secure':undefined,
        custom_map: {
          dimension20 : 'linkTitle_20',
          dimension21 : 'linkDestination_21',
          dimension113 : 'containerInfos_113',
          dimension128 : 'isSupervision_128',
          dimension19 : 'rawPagePath_19',
          dimension126 : 'eventCategory_126',
          dimension68 : 'mediaType_68',
          dimension127 : 'plStepLvl2_127',
          dimension117 : 'lastField_117',
          dimension136 : 'optinAds_136',
          dimension137 : 'optinAnalytics_137',
          dimension138 : 'optinPerso_138',
          dimension4 : 'logged_4',
          dimension10 : 'sourceAN_10',
          dimension27 : 'actionCo_27',
          dimension124 : 'rawReferrer_124',
          dimension125 : 'isBot_125',
          dimension103 : 'optinCategories_103',
          dimension141: 'hitOptinCategories_141',
          dimension66 : 'env_66',
          dimension115 : 'contextCode_115',
          dimension116 : 'stepNumber_116',
          dimension135 : 'bannerVersion_135',
          dimension_140 : 'sondes_140',
          dimension142: 'cmpLastClick_142',
          metric4 : 'cmpShow_4', 
          metric5 : 'cmpAnswer_5', 
          metric6 : 'optinAnalytics_6',
          metric7 : 'optinAds_7' 
        }
    });
});
tlz.oV('analytics', function(){
  //init
  tlz.gt('config', 'UA-33617477-8', {
      cookie_expires: 396 * 24 * 60 * 60,
      cookie_update: false,
      anonymize_ip: true,
      allow_google_signals: !!tlz.isOptin('ads'),
      allow_ad_personalization_signals: !!tlz.isOptin('ads'),
      site_speed_sample_rate: 10,
      content_group2: tlz._page.univers || '(not set)',
      content_group3: tlz._page.rawProduct || '(not set)',
      content_group4: tlz._page.product || '(not set)',
      content_group5: tlz._page.type || '(not set)',
      custom_map: {
          //dimensions
          dimension74: 'clientId', //natively replaced by true clientId
          dimension75: 'id1000Mercis_75',
          dimension8: 'userAgent_8',
          dimension66: 'env_66',
          dimension68: 'mediaType_68',
          dimension102: 'sessionId_102',
          dimension10: 'sourceAN_10',
          dimension27: 'actionCo_27',
          dimension124: 'rawReferrer_124',
          dimension19: 'rawPagePath_19',
          dimension126: 'eventCategory_126',
          dimension128: 'isSupervision_128',
          dimension103: 'optinCategories_103', // end dim generiques
          dimension1: 'userType_1',
          dimension4: 'logged_4',
          dimension6: 'remembered_6',
          dimension7: 'leadId_7',
          dimension20: 'linkTitle_20',
          dimension21: 'linkDestination_21',
          dimension22: 'linkNumber_22',
          dimension93: 'idType_93',
          dimension122: 'dynatraceCookie_122',
          dimension113: 'containerInfos_113',
          dimension5: 'agencyId_5',
          dimension134: 'privacyId_134',
          dimension135: 'privacyVersion_135',
          dimension136: 'optinAds_136',
          dimension137: 'optinAnalytics_137',
          dimension138: 'optinPerso_138',
          dimension_140 : 'sondes_140',
          dimension142: 'cmpLastClick_142',
          dimension146: 'csMatchingKey',
          //metrics
          metric2: 'views_2',
          metric3: 'clicks_3'
      }
  });
  tlz.oV('ads', function() {
      tlz.gt('set', { allow_google_signals: true, allow_ad_personalization_signals: true });
  });
});
tlz._setDimensions = function(name){
  //session dims
  tlz.oV('analytics',function(){
      tlz.x1('ga_session_dim_' + name, function() {
          tlz.gt('set', {
              userAgent_8: tlz.userAgent,
              env_66: tc_vars.env || '(not set)',
              sessionId_102: tlz._session.sessionId,
              sourceAN_10: tlz._session.sourceAN,
              actionCo_27: tlz._session.actionCo,
              rawReferrer_124: tlz.referrer && !tlz.contains(tlz.referrer, 'allianz.fr') && tlz.referrer || '(not set)',
              isSupervision_128: tlz._alz.email == tlz.sha256('supervision@allianz.fr') ? '1': '0'
          });
          tlz.oV('ads', function(){
              tlz.gt('set', 'dynatraceCookie_122', tlz.store.get('dtCookie'));
          });
      }, 'session');
  });
  //dims
  tlz.gt('set', {
      userType_1: tlz._alz.userType || 'prospect',
      logged_4: tlz._alz.logged || '0',
      remembered_6: tlz._alz.remembered || '0',
      rawPagePath_19: tlz.href,
      env_66: tc_vars.env,
      mediaType_68: tlz.getMediaType(654, 974),
      containerInfos_113: tlz.getContainersInfos(),
      eventCategory_126: tlz._eventCategory,
      optinAds_136: tlz.isOptin('ads') ? '1' : '0',
      optinAnalytics_137: tlz.isOptin('analytics') ? '1' : '0',
      optinPerso_138: tlz.isOptin('functional') ? '1' : '0',
      optinCategories_103: tlz.getOptinCategories(),
      hitOptinCategories_141: tlz.getOptinCategories(),
      sondes_140: tlz.userAgent.match(/iplabel|grandma|witbe/) ? '1' : '0'
  });
}
tlz._setDimensions('exempt');
tlz.oV('analytics', function(){
  tlz._setDimensions();
  tlz.x1('send pending events',function(){
    window.setTimeout(function(){
      tlz.doForEach(tlz._pendingGtEvents, function(gtEvent){
        if (tlz.contains(gtEvent[0], 'gtag')){ gtEvent.shift(); }
        if (!!gtEvent[2] && tlz.contains(gtEvent[2]['send_to'], tlz._alzExemptedGaID)){
          gtEvent[2]['send_to'] = tlz._alzGaID;
        }
        tlz.gt.apply(this, gtEvent);
      });
    },1);
  });
})
//path
tlz.gt('set', { page_path: tlz.customPath });
//app name
if (tlz.hostname == 'espace-particulier.allianz.fr' && (tlz.contains(tlz.path, 'espace-client') || tlz.contains(tlz.path, 'login'))){
  tlz.gt('set', 'app_name', 'espace_client_ow_login');
}
//id1000Mercis
tlz.setMacro('id1000Mercis', { user: 'alz', value: tlz.cookie.get('__troRUID') });
tlz._pageOpt = { send_to: tlz._getConsentGaIds() };
if (tlz._alz.id1000Mercis) {
    tlz._pageOpt.id1000Mercis_75 = tlz._alz.id1000Mercis;
} else {
    tlz.doWhen(function() { return !!tlz.cookie.get('__troRUID') }, function() {
      tlz.setMacro('id1000Mercis', { user: 'alz', value: tlz.cookie.get('__troRUID'), usage:'analytics' });
        tlz.x1('session_id_1000mercis', function() {
            tlz.gt('event', 'send tro ruid', { event_category: 'numberly', id1000Mercis_75: tlz._alz.id1000Mercis, non_interaction: true });
        }, 'session');
    }, function() { tlz.warn('no cookie "__troRUID" found') }, { attempsToCbkKo: 200 });
}
//pageview
if (!tlz.isIframe()) {
    tlz.x1('pageview ga', function() {
        if (!tlz._alz.clientIdGA) {
            tlz._pageOpt.event_callback = function() {
                tlz.x1('ga cbk', function() {
                    tlz.doWhen(function() { return !!tlz.getProp('window.ga.getAll') && !!tlz.getProp('window.ga.getAll')[0] }, function() {
                        tlz.setMacro('clientIdGA', { user: 'alz', value: window.ga.getAll()[0].get('clientId'), usage:['ads', 'analytics', 'functional'] });
                        tlz.evt.send('ga');
                    }, function() { tlz.warn('ga is not ready!') }, { attempsToCbkKo: 200 });
                });
            };
        }
        tlz.gt('event', 'page_view', tlz._pageOpt);
    });
}
// step
//path virtual page
if (tlz._page.stepName){
  tlz.gt('set', { page_path: tlz.path.replace(/form\/.+$/,'form')+'#'+tlz._page.stepName });
  tlz.gt('event', 'page_view', tlz._pageOpt);
}
//onga
tlz._onGa = function(cbk) {
    if (tlz._alz.clientIdGA || tlz._alz.clientIdGA) {
        cbk();
    } else {
        tlz.evt.on('ga', function() {
            cbk();
        });
    }
};
</script>
""")
    print(x)
    
test()




#Chcek .alz - vie - versements [53] tags "ga" // GOOD //
#Fikter cpn,tainer Google Tag Manager // GOOD //
#Eben,t tyê complete = conversion
#           generique = chargelent librairie
#           ta = conversion
#           mer = conversion
#           funnel = page
#            wcb = conversion
#           clic_mer_fq = conversion
#           demande d'activiation = conversion
#           inscription = conversion
#           global = chargelent librairie // GOOD //
#Bizarre tag not match container  // GOOD //
#Modife TagType si tlz.px alors px si tlz.js ou .js' alors js si les deux alors les deux // GOOD //
#Dans x1 time par defaut page si 3eme param n exste pas // GOOD //
#X1 Param mettre toute le param en brute // GOOD //
