<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1420680815127" ID="ID_872357754" MODIFIED="1420682816062" STYLE="fork" TEXT="database classes">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<font NAME="SansSerif" SIZE="12"/>
<node CREATED="1420680815127" ID="ID_1827600005" MODIFIED="1420682816062" POSITION="right" STYLE="fork" TEXT="Entry">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<font NAME="SansSerif" SIZE="12"/>
<node CREATED="1420681196128" ID="ID_1127701065" MODIFIED="1420682816062" STYLE="fork" TEXT="public(boolean)">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420681219161" ID="ID_1943370648" MODIFIED="1420682816062" STYLE="fork" TEXT="ocreddirectly(boolean)">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420681231794" ID="ID_694183812" MODIFIED="1420682816062" STYLE="fork" TEXT="idnumber(charfield(max_lenght=50)) #unix time + 10 random characters">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420681268004" ID="ID_730583317" MODIFIED="1420682816062" STYLE="fork" TEXT="codename(charfield(max_lenght=50))">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420681283261" ID="ID_827817397" MODIFIED="1420682816062" STYLE="fork" TEXT="entry_date(datetime) #for example, taken from screenshot filename">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420681304015" ID="ID_623094286" MODIFIED="1420682816062" STYLE="fork" TEXT="added_time(datetime) #when was it added to the database">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420681389572" ID="ID_1860320127" MODIFIED="1420682832782" STYLE="fork" TEXT="...positive integers &#x2014; stats">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420681030102" ID="ID_1610842320" MODIFIED="1420682816062" STYLE="fork" TEXT="Agent(foreign)">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<arrowlink COLOR="#b0b0b0" DESTINATION="ID_352195985" ENDARROW="Default" ENDINCLINATION="1;-9;" ID="Arrow_ID_1289193557" STARTARROW="None" STARTINCLINATION="-38;10;"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420681067944" ID="ID_183276702" MODIFIED="1420682816062" STYLE="fork" TEXT="creator(foreign)">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<arrowlink COLOR="#b0b0b0" DESTINATION="ID_5824134" ENDARROW="Default" ENDINCLINATION="188;19;" ID="Arrow_ID_1794631644" STARTARROW="None" STARTINCLINATION="425;0;"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420681100986" ID="ID_329114331" MODIFIED="1420682816061" STYLE="fork" TEXT="entry owner(foreign)">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<arrowlink COLOR="#b0b0b0" DESTINATION="ID_5824134" ENDARROW="Default" ENDINCLINATION="103;-24;" ID="Arrow_ID_938038661" STARTARROW="None" STARTINCLINATION="345;33;"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
</node>
<node CREATED="1420680909368" ID="ID_352195985" MODIFIED="1420682816061" POSITION="right" STYLE="fork" TEXT="Agent">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_352195985" ENDARROW="Default" ENDINCLINATION="1;-9;" ID="Arrow_ID_1289193557" SOURCE="ID_1610842320" STARTARROW="None" STARTINCLINATION="-38;10;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_352195985" ENDARROW="Default" ENDINCLINATION="-21;34;" ID="Arrow_ID_66394206" SOURCE="ID_864154926" STARTARROW="None" STARTINCLINATION="-151;16;"/>
<font NAME="SansSerif" SIZE="12"/>
<node CREATED="1420681422365" ID="ID_1043977055" MODIFIED="1420682816061" STYLE="fork" TEXT="codename">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420681433575" ID="ID_1077496355" MODIFIED="1420682816061" STYLE="fork" TEXT="database owner(foreign)">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<arrowlink COLOR="#b0b0b0" DESTINATION="ID_5824134" ENDARROW="Default" ENDINCLINATION="-62;21;" ID="Arrow_ID_131866013" STARTARROW="None" STARTINCLINATION="-275;50;"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420681991664" ID="ID_1135290791" MODIFIED="1420682816061" STYLE="fork" TEXT="creator(foreign)">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<arrowlink COLOR="#b0b0b0" DESTINATION="ID_5824134" ENDARROW="Default" ENDINCLINATION="-22;1;" ID="Arrow_ID_1239914306" STARTARROW="None" STARTINCLINATION="-236;44;"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420681444183" ID="ID_27418032" MODIFIED="1420682816061" STYLE="fork" TEXT="public(boolean)">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420681453632" ID="ID_1584119155" MODIFIED="1420682816061" STYLE="fork" TEXT="...contact information">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
</node>
<node CREATED="1420680915063" ID="ID_5824134" MODIFIED="1420682816061" POSITION="right" STYLE="fork" TEXT="User">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_5824134" ENDARROW="Default" ENDINCLINATION="188;19;" ID="Arrow_ID_1794631644" SOURCE="ID_183276702" STARTARROW="None" STARTINCLINATION="425;0;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_5824134" ENDARROW="Default" ENDINCLINATION="103;-24;" ID="Arrow_ID_938038661" SOURCE="ID_329114331" STARTARROW="None" STARTINCLINATION="345;33;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_5824134" ENDARROW="Default" ENDINCLINATION="-62;21;" ID="Arrow_ID_131866013" SOURCE="ID_1077496355" STARTARROW="None" STARTINCLINATION="-275;50;"/>
<linktarget COLOR="#b0b0b0" DESTINATION="ID_5824134" ENDARROW="Default" ENDINCLINATION="-22;1;" ID="Arrow_ID_1239914306" SOURCE="ID_1135290791" STARTARROW="None" STARTINCLINATION="-236;44;"/>
<font NAME="SansSerif" SIZE="12"/>
<node CREATED="1420681502210" ID="ID_1634296543" MODIFIED="1420682816061" STYLE="fork" TEXT="name">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420681671629" ID="ID_1445902161" MODIFIED="1420682816061" STYLE="fork" TEXT="email">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420681675837" ID="ID_864154926" MODIFIED="1420682816061" STYLE="fork" TEXT="ownagent(foreign)">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<arrowlink COLOR="#b0b0b0" DESTINATION="ID_352195985" ENDARROW="Default" ENDINCLINATION="-21;34;" ID="Arrow_ID_66394206" STARTARROW="None" STARTINCLINATION="-151;16;"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
<node CREATED="1420682120312" ID="ID_1728340866" MODIFIED="1420682816057" STYLE="fork" TEXT="settings">
<edge STYLE="sharp_bezier" WIDTH="2"/>
<font NAME="SansSerif" SIZE="12"/>
</node>
</node>
</node>
</map>
