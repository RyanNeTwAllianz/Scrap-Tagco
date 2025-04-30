def guess_event_type(tag_name: str) -> str:
    tag_name = tag_name.lower()

    keywords_map = {
        'page': ['page', 'pageview', 'funnel'],
        'conversion': ['lead', 'exclusion', ' mer ', 'conversions', 'event', 'souscription', 'conversion', 'purchase', 'contact', 'complete', ' ta ', ' mer ', ' wcb ', 'clic_mer_fq', 'inscription'],
        'config': ['consent mode'],
        'arrivee': ['form fq', 'arrivee', 'viewcontent', 'msg'],
        'chargement librairie': ['conteneur global', 'init', 'generique', 'global'],
        'visite': ['audience'],
        'audience': ['forfait_km']
    }

    for event_type, keywords in keywords_map.items():
        for keyword in keywords:
            if keyword in tag_name:
                return event_type

    return ''
