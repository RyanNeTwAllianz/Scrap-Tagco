from utils.GuessX1Time import guess_x1_time

def test () -> None:
    x = guess_x1_time("""
               <script type='text/javascript'> 
  
  if(typeof s !== 'undefined'){
    
    // EVARS    
    
    tlz._process = {};
    
    tlz._regexProcess = tlz._page.name.match(/(mer \w+) -/);
    if(tlz._regexProcess){
      tlz._process.name = tlz._regexProcess[1] + ' pl'; // mer agent - pl, mer email - pl, mer souscrire - pl
    } else{
      tlz._process.name = 'devis pl';
    }
    
    if(tlz.contains(tlz._page.name, 'confirmation')){
      tlz._process.status = 'confirmation'; 
    } else if(tlz._page.name == 'complete - avec tarif'){
      tlz._process.status = 'with tariff';
    } else if(tlz.path.match(/error|erreur/)){
      tlz._process.status = 'error';
    }
    
    // EVENTS
    
    s.events = apl(s.events,'event72'); // process step
    tlz.x1('process step by process id ' + tlz._page.product + tlz.angularPath + tlz._process.name, function(){
      s.events = apl(s.events,'event805'); // process step by process id
    });
    
    tlz._setEVarsStep(tlz._process.name, tlz._page.name || tlz.angularPath); // |previous process name azfr, stepName|stepNumber|previousStepName|previousStepNumber
    
    // Ã©tape 1, pl, mer agent, mer email
    tlz.x1('process view ' + tlz._page.product + tlz._process.name, function(){
      s.events = apl(s.events,'event32'); //process view
      s.events = apl(s.events,'event86=' + Date.now()); //process start time
    });
    
    // Ã©tape 1 pl
    if(tlz._process.name == 'devis pl'){
      tlz.x1('quote start ' + tlz._page.product + tlz._process.name, function(){
        s.events = apl(s.events,'event61'); //quote start
      });
    }
    
    // tarif pl mer confirmation
    if(tlz._page.name == 'complete - avec tarif' || tlz.contains(tlz._page.name, "confirmation") || tlz.contains(tlz.path, 'error') || tlz.contains(tlz.path, 'erreur')){
      tlz.x1('process complete ' + tlz._page.product + tlz._process.name, function(){
        s.events = apl(s.events,'event33'); //process complete
        s.events = apl(s.events,'event87=' + Date.now()); //process start time
      });
    }
    
    // tarif pl
    if(tlz._page.name == 'complete - avec tarif'){
      tlz.x1('quote generated ' + tlz._page.product + tlz._emp.tarif, function(){
        s.events = apl(s.events,'event62'); // quote generated
        s.events = apl(s.events,'event63=' + (tlz._emp.tarif || 'na')); // quote value 
      });
    }
    
    // lead
    if(tlz.contains(tlz._page.name, 'confirmation')){
      tlz.x1('lead aa by process id ' + tlz._page.product, function(){
        s.events = apl(s.events,'event801'); // lead by process id
      });
      tlz.x1('lead aa by product + risk + session' + tlz._page.product + tlz._emp.risk, function(){
        s.events = apl(s.events,'event802'); // lead by product + risk + session
      }, 'session');
      
      tlz.x1('lead aa  by 30j ' + tlz._page.product, function(){
        s.events = apl(s.events,'event804'); // lead by process id
      }, '30j');
      // ajouter lead by product + risk + X jours, et lead by product + risk + 30j
      s.eVar162 = {
        'mer agent - confirmation' : ('mer_agent_pl'),
        'mer email - confirmation' : ('mer_email_pl'),
        'mer souscrire - confirmation' : ('mer_souscrire_pl')
      }[tlz._page.name]; // exit lead type
    }
    
    // errors - pages d'erreurs
    if(tlz.contains(tlz.angularPath, 'error') || tlz.contains(tlz.angularPath, 'erreur')){
      //vars
      tlz._process.status = 'error';
      tlz._error = {};
      tlz._error.number = tlz.angularPath.match(/\d{3}/) && tlz.angularPath.match(/\d{3}/)[0];
      tlz._error.message = ({
        '400' : 'bad request',
        '401' : 'unauthorized',
        '403' : 'forbidden',
        '404' : 'page not found',
        '500' : 'internal server error'
      })[tlz._error.number];
      s.events = apl(s.events,'event97'); // error 
      s.eVar97 = ['http error', tlz._error.number, tlz._error.message].join('|'); // error nature|error code|error message
    }
    
    // cmp - show
    if((!tlz.cookie.get('OptanonConsent') || (tlz.getProp('cmp.closed')) && tlz._alz.userType != 'expert')){
      tlz.x1('cmp show', function(){
        s.eVar160 = tlz.getProp('cmp.config.name'); // banner version
        s.events = apl(s.events, 'event810'); // cmp views
      });
    }
    // cmp - answer
    if (tlz.getProp('cmp.closed') && tlz._alz.userType != 'expert'){
      tlz.x1('cmp answer', function(){
        s.eVar160 = tlz.getProp('cmp.config.name'); // banner version
        s.events = apl(s.events, 'event811'); // cmp answers
        if(tlz.getOptinCategories() == 'none'){s.events = apl(s.events, 'event807');} // cmp refuse
      });
    }
    
    // HIT
    
    s.t();
    s.clearVars();
  }

</script>




""")
    print(x)
    
test()