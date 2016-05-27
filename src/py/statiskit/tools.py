##################################################################################
#                                                                                #
# StatisKit: meta-repository providing general documentation and tools for the   #
# **StatisKit** Organization                                                     #
#                                                                                #
# Copyright (c) 2016 Pierre Fernique                                             #
#                                                                                #
# This software is distributed under the CeCILL-C license. You should have       #
# received a copy of the legalcode along with this work. If not, see             #
# <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.                 #
#                                                                                #
# File authors: Pierre Fernique <pfernique@gmail.com> (5)                        #
#                                                                                #
##################################################################################

def list_input(msg, items, default):
    answer = raw_input(msg + " [" + '/'.join(items)+ "]: ")
    while answer and answer not in items:
        answer = raw_input(msg + " [" + '/'.join(items)+ "]: ")
    if not answer:
        answer = default
    return answer
