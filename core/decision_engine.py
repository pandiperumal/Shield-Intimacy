def aggregate_signals(nsfw_score, ai_score, identity_found, is_shielded):
    """
    Stage 5: Deterministic Decision Logic
    """
    # Rule 1: Clear NCII Risk
    if nsfw_score > 0.6 and identity_found and is_shielded:
        return "CRITICAL_NCII_BLOCK"
    
    # Rule 2: Deepfake Abuse Risk
    if nsfw_score > 0.6 and ai_score > 0.8:
        return "POTENTIAL_DEEPFAKE_ABUSE"
    
    # Rule 3: Unverified Intimate Content
    if nsfw_score > 0.6 and not is_shielded:
        return "FLAGGED_FOR_HUMAN_REVIEW"
        
    return "SAFE_OR_RELEASE"