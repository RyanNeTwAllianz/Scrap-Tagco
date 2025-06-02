

data = [
    {
        'tool': 'cs',
        'script': '''<script type="text/javascript"> 
                tlz.oV('analytics', function(){
                    tlz.x1('listen lead cs', function(){
                    tlz.evt.on('lead',function(e){
                        tlz.x1('lead cs'+tlz._page.product+' '+tlz._form.risk,function(){
                        window._uxa = window._uxa || [];
                        window._uxa.push(['ec:transaction:create', {
                            'id': tc_vars.conversion_file_id,       /* obligatoire - ID de transaction ("string") */
                            'revenue': '1' /* obligatoire - Montant total de la transaction ("number" ou "string" compatible avec "parseFloat") */
                        }]);
                        window._uxa.push(['ec:transaction:items:add', {
                            'id': tc_vars.conversion_file_id,              /* obligatoire - ID de transaction ("string") */
                            'name': tlz._page.product,  /* obligatoire - Nom du produit ("string") */
                            'sku': tlz._page.rawProduct || tlz._page.product,          /* obligatoire - Code produit ("string") */
                            'category': 'lead',   /* optionnel   - CatÃ©gorie du produit ("string") */
                            'price': '1',          /* obligatoire - Prix du produit ("number" ou "string" compatible avec "parseFloat") */
                            'quantity': '1'           /* obligatoire - QuantitÃ© ("number" ou "string" compatible avec "parseFloat") */
                        }]);
                        window._uxa.push(['ec:transaction:send']);
                        },'session');
                    });
                    });
                });
                </script>''',
        'dupeKeyResult': 'id: tc_vars.conversion_file_id | id: tc_vars.conversion_file_id',
        'GuessDupeX1Result': "'listen lead cs' | 'lead cs'+tlz._page.product+' '+tlz._form.risk",
        'GuessTagTypeResult': 'js',
        'GuessX1TimeTest': 'session | page'
    },
    {
        'tool': 'cm',
        'script': '''<script type="text/javascript"> 
                    tlz.x1('listener lead cm', function(){
                        tlz.evt.on('lead', function(){
                        var product = ({
                            'auto': { group: 'am_count', tag: 'lead' },
                            'auto - outre-mer': { group: 'am_count', tag: 'lead' },
                            'auto voiturette' : { group: 'am_count', tag: 'lead-av' },
                            'auto collection' : { group: 'am_count', tag: 'lead-co' },
                            'moto': { group: 'am_count', tag: 'lead-m' },
                            'mrh': { group: 'mr_count', tag: 'lead' },
                            'mrh - outre-mer': { group: 'mr_count', tag: 'lead' },
                            'pno': { group: 'mr_count', tag: 'lead-pn' },
                            'sante pro': { group: 'sb_count', tag: 'lead' },
                            'sante par': { group: 'sc_count', tag: 'lead' },
                            'emprunteur': { group: 'em_count', tag: 'lead' },
                            'nvei': { group: 'am_count', tag: 'lead-nv' },
                            'malusse': { group: 'am_count', tag: 'lead-ma' },
                            'auto ultimo': { group: 'am_count', tag: 'lead-ma' },
                            'chien chat': { group: 'mr_count', tag: 'lead-ch' },
                            'camping car': { group: 'am_count', tag: 'lead-cc' },
                            'bateau': { group: 'mr_count', tag: 'lead-bt' },
                            'scolaire': { group: 'mr_count', tag: 'lead-sc' },
                            'pj': { group: 'mr_count', tag: 'lead-pj' },
                            'auto pro': { group: 'am_count', tag: 'lead-ap' },
                            'startup': { group: 'pr_count', tag: 'lead-su' },
                            'multi pro': { group: 'pr_count', tag: 'lead-ml' },
                            'prevoyance': { group: 'sb_count', tag: 'lead-pv' },
                            'pro': { group: 'pr_count', tag: 'lead-ot' },
                            'gav': { group: 'mr_count', tag: 'lead-gv' },
                            'retraite': { group: 'av_count', tag: 'lead-ri' },
                            'velo': { group: 'mr_count', tag: 'lead-vl' },
                            'sante': { group: 'sc_count', tag: 'lead' } 
                        })[tlz._page.product];
                        if (product){
                            var cmParams = {
                            send_to: 'DC-8289986/' + product.group + '/' + product.tag + '+per_session',
                            session_id: tlz._session.sessionId + tlz._form.risk,
                            u1: tlz._page.parcoursType, //page_parcours_type ['fq','pl','souscription','form']
                            u2: tlz._page.product.replace(/ /g,'-'), //page_product ['mrh','auto','moto','sante par','sante pro']
                            u4: tlz.device(), //user_device ['desktop','tablet','mobile']
                            u5: tlz._alz.userType || 'prospect', //user_type ['prospect','client']
                            u6: tlz.contains(tlz._page.action, 'wcb') ? 'wcb' : 'form',
                            u11: tlz._form.model,
                            u12: tlz._form.brand,
                            u14: tlz._form.type,
                            u16: tlz._form.roomNb,
                            u20: tlz._page.product.replace(/ /g,'-'),
                            u21: tlz._alz.logged == '1' ? 'logge' : 'non logge', //user_visitor_log ['logge','non logge']
                            u22: tlz._alz.clientIdGA, //user_ga360id
                            u24: '/formulaire-devis-' + tlz._page.product + '/' + tlz._stepNumber + '-' + tlz.norm(tc_vars.form_step_name).replace(' ', '-'), //page_uri_sans_param
                            u25: tlz.topDomain.replace('.fr', ''), //page_domain ['allianz','allsecur','eallianz']
                            u26: tlz.norm(tlz.title), //page_page_title
                            u28: 'site', //page_interface ['site','chatbot']
                            u29: tlz._page.productType, //page_type ['professionnel','particulier']
                            u33: tlz._page.name, // form step name
                            u34: tlz._form.idDevis,
                            u35: tlz._session.sessionId,
                            u37: tlz._loadedTms, // tms version
                            allow_custom_scripts: true
                            };
                            if(!tlz.isOptin('ads')){
                            tlz.doForEach(['u8', 'u22', 'u34', 'u35', 'u36', 'session_id'], function(v){ // if not optin, remove post code, id devis, id affilie, id ga, id session
                                delete cmParams[v];
                            });
                            }
                            tlz.gt('event', 'conversion', cmParams); // lead forms
                            var cmParams2 = tlz.clone(cmParams);
                            cmParams2.send_to = 'DC-8289986/az_count/lead+per_session';
                            if(tlz.isOptin('ads')){
                                cmParams2.session_id = tlz._session.sessionId + tlz._page.product;
                            }
                            tlz.gt('event', 'conversion', cmParams2) // lead global
                        }
                        });
                    });
                    </script>''',
        'dupeKeyResult': 'session_id: tlz._session.sessionId + tlz._form.risk',
        'GuessDupeX1Result': "'listener lead cm'",
        'GuessTagTypeResult': "js",
        'GuessX1TimeTest': 'page'
    }
]