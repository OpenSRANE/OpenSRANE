# /* ****************************************************************** **
# **   OpenSRANE - Open Software for Risk Assessment of Natech Events   **
# **                                                                    **
# **                                                                    **
# **                                                                    **
# ** (C) Copyright 2023, Mentioned Regents in 'COPYRIGHT' file.         **
# **                                                                    **
# ** All Rights Reserved.                                               **
# **                                                                    **
# ** Commercial use of this program without express permission of the   **
# ** owner (The Regents), is                                            **
# ** strictly prohibited.  See file 'COPYRIGHT'  in main directory      **
# ** for information on usage and redistribution,  and for a            **
# ** DISCLAIMER OF ALL WARRANTIES.                                      **
# **                                                                    **
# ** Developed by:                                                      **
# **   Bijan SayyafZadeh (OpenSRANE@Gmail.com)                          **
# **   MehDi Sharifi                                                    **
# **   Abdolreza S. Moghadam                                            **
# **   Eslam Kashi                                                      **
# **                                                                    **
# ** ****************************************************************** */

'''
 Written: Bijan Sayyafzadeh
 Created: 2022
 
 Revision: -
 By & Date: -
'''


import os


def string():
    try:
        with open(os.path.dirname(__file__) + "/VERSION", "r", encoding="utf-8") as fh:
            version = fh.read().strip()
            if version:
                return version
    except:
        pass
    return "unknown (git checkout)"
