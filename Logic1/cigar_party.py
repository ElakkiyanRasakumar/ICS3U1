def cigar_party(cigars, is_weekend):
    if is_weekend and cigars >= 40:
        return True
    elif not is_weekend:
        if 40 <= cigars <= 60:
            return True
        else:
            return False
    else:
        return False

    # return (is_weekend and cigars >= 40) or (not is_weekend and 40 <= cigars <= 60) - I had a feeling it could be done on one line. NOT MY SOLUTION