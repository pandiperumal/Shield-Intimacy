def aggregate_signals(nsfw_score, identity_found, is_shielded, ai_score):
    if is_shielded:
        if ai_score > 0.4 and nsfw_score > 0.7:
            return "CRITICAL_AI_NCII_BLOCK"
        
        if ai_score <= 0.4 and nsfw_score > 0.7:
            return "CRITICAL_NCII_BLOCK"
            
        if ai_score > 0.4 and nsfw_score <= 0.7:
            return "SYNTHETIC_IDENTITY_BLOCK"
            
        return "RISKY_SAFE_MATCH"

    if ai_score > 0.4:
        return "APPROVED_SYNTHETIC_CONTENT"

    if nsfw_score > 0.7:
        return "POTENTIAL_NSFW_CONTENT"

    return "SAFE_OR_RELEASE"