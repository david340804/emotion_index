import re
import os,sys

#file that contains the flag library
filename  = 'rose.txt'
with open(filename) as f:
    words = f.readlines()

d = {}

#import flags and markers from text file
# a flag is an index, markers are the associated words whose occurences are summed to determine the flag value for a string
for line in words:
    #take off trailing whitespace and newlines
    line = line.strip()

    #separate flag and markers
    line = line.split(':')
    flag = line[0]
    markers = line[1].split(',')

    #add to dictionary
    d[flag] = markers


input_string = '''HOUSTON — The Trump administration delivered a setback to Exxon Mobil on Friday, announcing that it would not grant the oil giant a waiver from sanctions against Russia that would allow drilling in the Black Sea. The decision, reinforcing barriers erected by the United States over Russia’s intervention in Ukraine, was another sign that President Trump has been unwilling or unable to improve relations with the Kremlin early in his term, after pledging as a candidate that he would seek a thaw. “In consultation with President Donald J. Trump,” Treasury Secretary Steven Mnuchin said in a terse, prepared statement, “the Treasury Department will not be issuing waivers to U.S. companies, including Exxon, authorizing drilling prohibited by current Russian sanctions.” The prospect of a waiver had drawn denunciations from both Democratic and Republican lawmakers. When news of Exxon Mobil’s proposal emerged this week, Senator John McCain, Republican of Arizona, wrote in a Twitter post, “Are they crazy?” The matter was complicated by the continuing congressional scrutiny of reports of Russian intervention in support of Mr. Trump in last year’s election, and by Secretary of State Rex W. Tillerson’s role as Exxon Mobil’s chief executive until the president nominated him for his current position. Exxon Mobil applied for the waiver in 2015, arguing that it could lose its exploration rights in the Black Sea if it did not begin drilling operations by the end of 2017 under its contract with the Russian state oil company Rosneft. The Obama administration did not act on the application, but Exxon Mobil hoped that the Trump administration would take a favorable view. The company released a brief statement on Friday that did not express regret but explained its argument in favor of the waiver. “We understand the statement today by Secretary Mnuchin in consultation with President Trump,” the statement said. “Our 2015 application for a license under the provisions outlined in the U.S. sanctions was made to enable our company to meet its contractual obligations under a joint venture agreement in Russia, where competitor companies are authorized to undertake such work under European sanctions.” DealBook DealBook delivers the news driving the markets and the conversation. Delivered weekday mornings and afternoons. Enter your email address Sign Up Receive occasional updates and special offers for The New York Times's products and services. SEE SAMPLE PRIVACY POLICY United States and European sanctions were first imposed on Russia in March 2014 in response to Moscow’s annexation of Crimea from Ukraine. Exxon Mobil signed an expansion of its joint venture projects anyway, even after Igor I. Sechin, Rosneft’s chief executive, was personally blacklisted in connection with the sanctions. The deal was legal, but Exxon Mobil was more fully constrained when tighter sanctions were imposed after Russia was implicated that summer in the shooting down of Malaysia Airlines Flight 17 over eastern Ukraine. It has become increasingly clear in recent days that relations between the United States and Russia are unlikely to improve any time soon. Mr. Tillerson has used increasingly tough talk to highlight the Trump administration’s differences with Russia over its alliance with the Syrian government. He has not suggested that any sanctions be lifted, and the administration has affirmed its commitment to the North Atlantic Treaty Organization and European security. Exxon Mobil’s hopes to produce new oil in Arctic waters and in Siberian shale fields were delayed indefinitely by the toughened sanctions, which prohibited transfers of drilling technology capable of reaching oil in fields that previously had been virtually inaccessible. The company received a few exceptions to the sanctions, including a waiver in late 2014 that allowed it complete drilling of one exploration well in the frigid Kara Sea that it said would be unsafe to leave half finished. A big oil field was confirmed, but no new oil was produced and exported. Exxon Mobil has long argued that it was being put at a disadvantage against some of its European competitors operating in Russia. ENI, the Italian oil giant, plans to drill this year in the Black Sea, a largely untapped area with enormous oil reserve potential. European sanctions are somewhat weaker than those imposed by the United States since they exempted some contracts signed before the sanctions were put in place. The American sanctions drew a harder line. Exxon Mobil’s drilling rights in the Black Sea were part of a sweeping strategic partnership Exxon Mobil developed with Rosneft in 2011 while Mr. Tillerson was in charge of the American company. The agreement came at a time when the Obama administration was seeking to improve relations with Russia, and several Western oil companies expanded their operations.'''
input_string2 = 'Im sleeping with my cat'

#record of flag occurences
rec  = {}

for key,vals in d.items():
    #iterate over flags

    #zero the record
    rec[key] = 0
    
    for word in vals:
        #once per word in this flag
        count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word.lower()), input_string.lower()))

        #add one to the record of
        rec[key] = rec[key] + count


print(rec)
