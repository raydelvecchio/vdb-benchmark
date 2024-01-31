from vlite2 import VLite2
from vlite import VLite
from vlite2.utils import chop_and_chunk
from chromadb.utils import embedding_functions
import os
import time
import glob
import timeit
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import weaviate
import weaviate.classes as wvc

short_data: str = "Hello! My name is Ray. How are you?"
long_data: str = ''.join(["28 \n One of the notable characteristics of legal science is its emphasis on definitions, classifications, and a \nprecise legal vocabulary. Scholars strive for the validity of concepts and classes, treating them as \nexpressio ns of scientific truth rather than conventional or utilitarian constructs  . \nLegal science seeks to be pure and value -free, focusing solely on legal phenomena and excluding influences \nfrom social sciences or historical context. It emphasizes legal values suc h as certainty in the law and \nexcludes considerations of justice or societal ends, which are seen as the domain of legal philosophy  . \nDespite criticism and various reactions, legal science continues to dominate legal scholarship in civil law \njurisdictions. It is deeply ingrained in legal education, textbooks, and the legal system itself. While the \ncommon law tradition has not fully embraced legal science, occasional trends towards its thinking have \nbeen observed . \nOverall, legal science represents a systemati c and highly abstract approach to studying and understanding \nthe law within the civil law tradition. It has had a profound influence on legal scholarship and the legal \nsystems of many countries . \n \nReading 7    \nשיעור שני  \nLegrone: how legrone views the purpos e of comparative law   ? \nLagron sees the benefits of comparative law – it helps us see our society in a better way  . \nEven the word judge means different things in different countries. If we wont have the understanding that \nthis things are different between c ountries, it will be very hard for us to communicate   . \n- According to lagron, we should look at the wider picture, not only the legal system, but the legal \nculture  . \n- LaGrone opens us to an external perspective. He says we should look at the legal system inside the \nbroader cultural, economical and social aspects . \n- Lagrone says no law is shaped by history. We have difference that changes overtime  . \n- Lagrone talks about  the idea of contingency. The law reflects the values of the society we live in   . \nKey aspects of the development of civil law tradition  : \nTradition was roughly speaking around the year 1000 it's really in this. That these three separate traditions \nof Roman law Canon law commercial law begin to develop in ways that lead to their eventual kind of \nconvergence and I think really really importantly it's at around exactly this time you know give or take the \nyear 1000 that we can begin to see the origins of what wi ll become the major European states right so the \nFrench capetian monarchy right begins in the late ten 10th century the holy Roman Empire which is where \nwe get modern Germany right that is typically dated to starting in 962 England in its modern form with the \nNorman conquest that takes place in 1066 and this is really crucial right in the west law and the state \nemerged at the same time and law is central to the project of state building in the west right and i think this \nis this is really key for understand ing law in the west  . \nRoman law: I mean as Roman law in its modern incarnation Roman law as we discovered after the fall of the \nRoman Empire right so the Roman Empire after surviving for like 5 centuries collapses around the 5th and \n6th centuries when we ha ve an invasion of various Germanic tribes right coming from the the the North \nEast and north and for another five centuries or so from the collapse of Rome we have the period of the \nearly Middle Ages that used to be called the dark ages that is no longer t he politically correct term right but", '110 \n the diminishing importance of religious obligations, and the regulation of family relationships by the state. \nNationalism played a role in the revolution, aiming to establish national legal systems that reflected national \nideals and unity.  \nWhile the revolution brought about significant changes and introduced important ideas, it also had some \nexaggerations and utopian aspirations. The legal systems in many civil law countries bear the influence of the \nfervent utopianism of t he French Revolution, including the emphasis on the separation of powers, the \nestablishment of administrative courts, and the distinction between public and private law.  \nOverall, the revolution had a profound impact on public law, the organization and admi nistration of legal \nsystems, and the principles and concepts embedded in the basic codes of civil law jurisdictions.  \nThe passage discusses the sources of law in civil law and common law traditions. In civil law systems, the \nprimary sources of law are statu tes enacted by the legislative power, regulations issued by administrative \nagencies, and custom. The legislative power holds a monopoly on lawmaking, and judicial decisions are not \nconsidered law. The passage also mentions the growing influence of constitu tionalism, with written \nconstitutions gaining importance as a source of law and constitutional courts exercising judicial review. In \ncontrast, common law systems rely on a combination of statutes, judicial decisions, and customary practices. \nThe distinctio n between civil law and common law systems cannot be simply reduced to the presence or absence \nof codes. The ideology behind codification in civil law systems is rooted in the French Revolution and seeks to \nestablish a new legal order by repealing prior la w and unifying diverse legal systems.  \nIn the common law world, judges are highly respected and influential figures who shape and interpret the law \nthrough their decisions. They are seen as culture heroes and their names are well -known. Judges in this system \nhave broad interpretative powers, including the ability to review administrative actions and declare legislation \nunconstitutional. Common law judges often have successful legal careers before being appointed or elected to \nthe bench, and their positi ons bring them respect, prestige, and public attention.  \nIn contrast, judges in the civil law world have a different role and status. They are considered civil servants and \nfunctionaries rather than culture heroes. Civil law judges are selected from the ran ks of the professional \njudiciary, typically through a state examination or attendance at a special school for judges. They rise in the \njudiciary based on demonstrated ability and seniority, and their salaries and working conditions are a focus of \ntheir pro fessional organization. Lateral entry into the judiciary is rare, and judges are primarily selected from \nwithin the judiciary itself.  \nThe different status of civil law judges can be traced back to the historical development of the civil law tradition, \nwher e judges were not prominent figures of the law and had limited power. With the establishment of rigid \nconstitutions and the introduction of judicial review in some civil law jurisdictions, the role of judges has \nevolved to include constitutional review. Ho wever, the traditional image of civil law judges as bureaucratic \ncivil servants performing mechanical functions still persists to some extent.  \nIn recent years, there has been a trend towards increased judicial scope and power in the civil law tradition. \nSpecial constitutional courts have been established in some jurisdictions, and ordinary judges can reject the \napplication of statutes if they consider them unconstitutional. Scholars and the media have noted a growing \njudicial protagonism in some civil law c ountries, and the role of judges is being reexamined and analyzed.', '109 \n of enacted propositions rather than practical knowledge. The idea of a common European legal system has been \npromoted by various individuals and institutions, with proposals for a European Code of Private Law and \nEuropean restatements of contr act law. However, the author challenges the notion of convergence, arguing that \nfocusing solely on rules and concepts overlooks the ephemeral and contingent nature of laws. Rules are seen as \nbrittle and lacking universal merit, while concepts are seen as p eremptory instruments that do not fully capture \nthe complexity of legal systems.  \nThe text argues that to understand societies and the legal cultures they have produced, one must move away \nfrom rules and concepts and focus on habits and customs. The author suggests that a synecdochic view of the \nlaw, where rules and concepts represent the whole, is insufficient. Instead, the focus should be on the cognitive \nstructure and epistemological foundations of a legal culture, referred to as the "legal mentality." Th e author \nemphasizes the importance of examining assumptions, attitudes, aspirations, and antipathies to uncover the \ndeep structures of legal rationality. The text further discusses the differences between common law and civil \nlaw mentalities and asserts th at these differences are irreducible at the epistemological level. The author argues \nagainst the idea of European legal integration, stating that the differences between legal mentalities make \nconvergence impossible. The text highlights the significance of  longue durée and the interiorization of culture \nin understanding legal mentalities. The author acknowledges the pluralistic nature of industrial societies and \naims to identify a representative common core within legal cultures. Overall, the text emphasize s the importance \nof cognitive structures and epistemological differences in studying legal cultures and rejects the notion of \nconvergence between common law and civil law traditions.  \n \nReading 6 – The Revolution  \nThe passage discusses the impact of a revolution that occurred in the West starting in 1776, which influenced \nthe development of public law in civil law jurisdictions. This revolution, encompassing events such as the \nAmerican and French revolutions, the Italian Risorgimento, and the liberation  movements in Latin America, \nbrought about a fundamental intellectual and social revolution. It challenged long -established ideas about \ngovernment and the individual and introduced new ways of thinking about humanity, society, the economy, and \nthe state.  \nThe revolution led to significant changes in public law and also influenced the form, application, and content \nof the basic codes derived from Roman and jus commune sources. One of the driving forces behind the \nrevolution was secular natural law, which emph asized the equality of all individuals and their natural rights to \nproperty, liberty, and life. The revolution also promoted the separation of governmental powers, particularly \nthe separation of legislative, executive, and judicial powers. This separation aimed to prevent the judiciary from \ninterfering in lawmaking and the execution of laws.  \nThe revolution had a different impact on public law in different regions. In France, for example, it targeted the \njudicial aristocracy due to their alignment with the l anded aristocracy and their blurred distinction between \napplying and making law. In contrast, the United States and England had a different judicial tradition, with \njudges often playing a progressive role in protecting individuals against abuse of power an d contributing to the \ncentralization of governmental power.  \nThe revolution was characterized by an emphasis on reason, individual rights, and the transition from feudalism \nto contract -based relationships. It also glorified the secular state, leading to the  abolition of feudal obligations,', '25 \n The text  : \nHe is talking about an evolution between the French code and the present, he is talking about Europe and \nthe US. He thinks that it is very common in 1900 that _______, it was an age that people that though about \nthe law in a positive way, the law was the law of the people. It\'s connected to normative point: he said they \nscrew us up, there is no way to see  the law in a positive way, to understand it you have to break. What came \nout of it? He will say that we can do comparative law for understanding the best solution for legal problems. \nWe supposed to help each other find the right answer, like there is one .  \nWhat is the law? What is the unit that he\'s is rules, legal rules. This fits the science model, formalistic   . \nHow do you think of law comparing that change over time? He\'s looking for progress, working with each \nother to get better answers   . \nIs that real ly the case? Who define what the best law is? There is different ideas and there are different \nproblems in the world . \nSummary    : \n       \n \nReading 5 – European legal systems are not converging  \nThe text discusses the convergence of European legal systems. It n otes that economic factors have led \nWestern European countries to pursue a supra -national legal order, resulting in the creation of the \nEuropean Community. While most of these countries follow the "civil law" tradition, the European \nCommunity\'s focus on ha rmonization and integration has led to the development of a complex network of \ninterconnected laws and regulations. The text suggests that a common European law, or "corpus juris \nEuropaeum," would likely consist of enacted propositions rather than practica l knowledge. The idea of a \ncommon European legal system has been promoted by various individuals and institutions, with proposals \nfor a European Code of Private Law and European restatements of contract law. However, the author \nchallenges the notion of con vergence, arguing that focusing solely on rules and concepts overlooks the \nephemeral and contingent nature of laws. Rules are seen as brittle and lacking universal merit, while \nconcepts are seen as peremptory instruments that do not fully capture the compl exity of legal systems  . \nThe text argues that to understand societies and the legal cultures they have produced, one must move \naway from rules and concepts and focus on habits and customs. The author suggests that a synecdochic \nview of the law, where rules and concepts represent the whole, is insufficient. Instead, the focus should be \non the cognitive structure and epistemological foundations of a legal culture, referred to as the "legal \nmentality." The author emphasizes the importance of examining ass umptions, attitudes, aspirations, and \nantipathies to uncover the deep structures of legal rationality. The text further discusses the differences \nbetween common law and civil law mentalities and asserts that these differences are irreducible at the \nepistem ological level. The author argues against the idea of European legal integration, stating that the \ndifferences between legal mentalities make convergence impossible. The text highlights the significance of \nlongue durée and the interiorization of culture in  understanding legal mentalities. The author acknowledges \nthe pluralistic nature of industrial societies and aims to identify a representative common core within legal \ncultures. Overall, the text emphasizes the importance of cognitive structures and episte mological \ndifferences in studying legal cultures and rejects the notion of convergence between common law and civil \nlaw traditions  .', '111 \n Overall, while common law judges are seen as central figures in shaping and interpreting the law, civil law \njudges traditionally have more limited roles and are viewed as functionaries. How ever, there are ongoing \nchanges and developments in the civil law tradition that are expanding the scope and power of judges.  \nLegal science, also known as systematic jurisprudence or conceptual jurisprudence, is a dominant school of \nthought within the civi l law tradition. It emerged in the 19th century and is primarily associated with German \nlegal scholars. Legal science emphasizes the scientific study of law and seeks to discover inherent principles \nand relationships within legal materials. It aims to crea te a systematic and coherent legal structure by developing \nabstract concepts and classifications.  \nThe scholars of legal science focused on the principles of Roman civil law, particularly as it existed in Germany, \nand produced highly systematic treatises ba sed on their study of the Digest of Justinian. Their work culminated \nin the promulgation of the German Civil Code in 1896, which had a significant influence on legal scholarship \nworldwide.  \nLegal science adopts a highly systematic and logical approach, simi lar to that of natural sciences. It employs \nformal logic and logical expansion to reason from specific cases and principles to broader principles and \ntheories. This process aims to create a general theory of law that is abstract and detached from concrete \nproblems.  \nOne of the notable characteristics of legal science is its emphasis on definitions, classifications, and a precise \nlegal vocabulary. Scholars strive for the validity of concepts and classes, treating them as expressions of \nscientific truth rather  than conventional or utilitarian constructs.  \nLegal science seeks to be pure and value -free, focusing solely on legal phenomena and excluding influences \nfrom social sciences or historical context. It emphasizes legal values such as certainty in the law and excludes \nconsiderations of justice or societal ends, which are seen as the domain of legal philosophy.  \nDespite criticism and various reactions, legal science continues to dominate legal scholarship in civil law \njurisdictions. It is deeply ingrained in legal education, textbooks, and the legal system itself. While the common \nlaw tradition has not fully embraced legal science, occasional trends towards its thinking have been observed.  \nOverall, legal science represents a systematic and highly abstract appr oach to studying and understanding the \nlaw within the civil law tradition. It has had a profound influence on legal scholarship and the legal systems of \nmany countries.  \n \n \nReading 8 - The Current State of Legal Education Reform in Latin America: A Critical Appraisal Juny \nMontoya  \nThe article discusses the current state of legal education reform in Latin America. It highlights the challenges \nof inequality and social exclusion in the region and the need for lawyers who are equipped to address these \nissues. Trad itional legal education is criticized for leaving lawyers ill -prepared for these challenges. The article \nexamines efforts to reform legal education in several Latin American countries, including Brazil, Chile, \nArgentina, Mexico, Colombia, and Venezuela. It  explores the characteristics of legal education in the region'])
default_ef = embedding_functions.DefaultEmbeddingFunction() #for cdb

def startup_v1():
    v1 = VLite()

def startup_v2():
    v2 = VLite2()

def memorize_one_v1(v):
    v.memorize(short_data)

def memorize_one_v2(v):
    v.ingest(short_data)

def memorize_one_cdb(cdb):
    cdb.add(
        documents = [short_data],
        embeddings = default_ef([short_data]),
        ids = ["id0"],
    )

def memorize_one_pc(index):
    short_data_embeddings = SentenceTransformer('all-MiniLM-L6-v2').encode(short_data).tolist()
    index.upsert(vectors=[
        {"id": "id0", "values": short_data_embeddings}
    ])

def memorize_one_w(client):
    short_data_embeddings = SentenceTransformer('all-MiniLM-L6-v2').encode(short_data).tolist()
    with client.batch as batch:
        batch.add_data_object(
            data_object={"test": short_data_embeddings},
            class_name="Question"
        )

def remember_v1(v, text):
    v.remember(text)

def remember_v2(v, text):
    v.retrieve(text)

def remember_cdb(cdb, text):
    results = cdb.query(
        query_texts=[text],
    )

def remember_pc(index, text):
    text = SentenceTransformer('all-MiniLM-L6-v2').encode(text).tolist()
    query_response = index.query(
        namespace="ns0",
        vector=text,
        top_k=10
    )

def remember_w(client, text):
    text = SentenceTransformer('all-MiniLM-L6-v2').encode(text).tolist()
    response = (
        client.query
        .get("Question", ["test"])
        .with_near_text({"concepts": text})
        .do()
    )

def memorize_many_v1(v):
    v.memorize(text=long_data)

def memorize_many_v2(v):
    v.ingest(text=long_data)

def memorize_many_cdb(cdb):
    long_data_chunked = chop_and_chunk(long_data, 512)
    cdb.add(
        documents = long_data_chunked,
        embeddings = default_ef(long_data_chunked),
        ids = ["id"+str(i) for i in range(len(long_data_chunked))],
    )

def memorize_many_pc(index):
    long_data_chunked = chop_and_chunk(long_data, 512)
    long_data_embeddings = SentenceTransformer('all-MiniLM-L6-v2').encode(long_data_chunked).tolist()
    for i in range(len(long_data_chunked)):
        index.upsert(vectors=[
            {"id": "id"+str(i), "values": long_data_embeddings[i]}
        ])

def memorize_many_w(client):
    long_data_chunked = chop_and_chunk(long_data, 512)
    long_data_embeddings = SentenceTransformer('all-MiniLM-L6-v2').encode(long_data_chunked).tolist()
    with client.batch as batch:
        for i in range(len(long_data_embeddings)):
            batch.add_data_object(
                data_object={"test": long_data_embeddings[i]},
                class_name="Question"
            )

if __name__ == "__main__":
    start_time = time.time()

    num_executions = 100

    # startup_v1_time = timeit.timeit('startup_v1()', 
    #                            setup='from __main__ import startup_v1; from vlite import VLite',
    #                            number=num_executions) / num_executions
    
    # startup_v2_time = timeit.timeit('startup_v2()', 
    #                         setup='from __main__ import startup_v2; from vlite2 import VLite2',
    #                         number=num_executions) / num_executions

    memorize_one_v1_time = timeit.timeit('memorize_one_v1(v)', 
                        setup='''
from vlite import VLite
from __main__ import memorize_one_v1
v = VLite()
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE ONE V1")
    
    memorize_one_v2_time = timeit.timeit('memorize_one_v2(v)', 
                        setup='''
from vlite2 import VLite2
from __main__ import memorize_one_v2
v = VLite2()
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE ONE V2")
    
    memorize_one_cdb_time = timeit.timeit('memorize_one_cdb(collection)', 
                        setup='''
import chromadb
from chromadb.utils import embedding_functions
from __main__ import memorize_one_cdb
client = chromadb.Client()
collection = client.create_collection(name="collection")
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE ONE CDB")
    
    memorize_one_pc_time = timeit.timeit('memorize_one_pc(index)', 
                        setup='''
from pinecone import Pinecone, PodSpec
import os
from dotenv import load_dotenv
from __main__ import memorize_one_pc
load_dotenv(dotenv_path='.env', verbose=True)
pc = Pinecone(api_key=os.getenv('PC_API_KEY'))
for i in pc.list_indexes():
    if i['name'] == "quickstart":
        pc.delete_index(i['name'])
pc.create_index(name="quickstart", dimension=384, metric="cosine", spec=PodSpec(environment='gcp-starter'))
index = pc.Index("quickstart")
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE ONE PC")
    
    memorize_one_w_time = timeit.timeit('memorize_one_w(client)', 
                        setup='''
import weaviate
import weaviate.classes as wvc
import os
from dotenv import load_dotenv
from __main__ import memorize_one_w
load_dotenv(dotenv_path='.env', verbose=True)
client = weaviate.Client(
    url = "https://test-i6cwsfxe.weaviate.network",
    auth_client_secret=weaviate.auth.AuthApiKey(api_key=os.getenv('W_API_KEY')),
)
class_obj = {
    "class": "Question",
    "vectorizer": "none",
}
client.schema.delete_class("Question")
client.schema.create_class(class_obj)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE ONE W")

    remember_one_v1_time = timeit.timeit('remember_v1(v, "hello")', 
                        setup='''
from vlite import VLite
from __main__ import remember_v1
v = VLite()
v.memorize("Hello! My name is Ray. How are you?")
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER ONE V1")
    
    remember_one_v2_time = timeit.timeit('remember_v2(v, "hello")', 
                        setup='''
from vlite2 import VLite2
from __main__ import remember_v2
v = VLite2()
v.ingest("Hello! My name is Ray. How are you?")
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER ONE V2")
    
    remember_one_cdb_time = timeit.timeit('remember_cdb(collection2, "hello")', 
                        setup='''
import chromadb
from chromadb.utils import embedding_functions
from __main__ import remember_cdb
client = chromadb.Client()
collection2 = client.create_collection(name="collection2")
collection2.add(
        documents = ["Hello! My name is Ray. How are you?"],
        ids = ["id1"],
    )
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER ONE CDB")
    
    remember_one_pc_time = timeit.timeit('remember_pc(index, "hello")', 
                        setup='''
from pinecone import Pinecone, PodSpec
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv
from __main__ import memorize_one_pc, remember_pc
load_dotenv(dotenv_path='.env', verbose=True)
pc = Pinecone(api_key=os.getenv('PC_API_KEY'))
for i in pc.list_indexes():
    if i['name'] == "quickstart":
        pc.delete_index(i['name'])
pc.create_index(name="quickstart", dimension=384, metric="cosine", spec=PodSpec(environment='gcp-starter'))
index = pc.Index("quickstart")
memorize_one_pc(index)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER ONE PC")
    
    remember_one_w_time = timeit.timeit('remember_w(client, "hello")', 
                        setup='''
import weaviate
import weaviate.classes as wvc
import os
from dotenv import load_dotenv
from __main__ import memorize_one_w, remember_w
load_dotenv(dotenv_path='.env', verbose=True)
client = weaviate.Client(
    url = "https://test-i6cwsfxe.weaviate.network",
    auth_client_secret=weaviate.auth.AuthApiKey(api_key=os.getenv('W_API_KEY')),
)
class_obj = {
    "class": "Question",
    "vectorizer": "none",
}
client.schema.delete_class("Question")
client.schema.create_class(class_obj)
memorize_one_w(client)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER ONE W")


    memorize_many_v1_time = timeit.timeit('memorize_many_v1(v)', 
                        setup='''
from vlite import VLite
from __main__ import memorize_many_v1
v = VLite()
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE MANY V1")
    
    memorize_many_v2_time = timeit.timeit('memorize_many_v2(v)', 
                        setup='''
from vlite2 import VLite2
from __main__ import memorize_many_v2
v = VLite2()
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE MANY V2")

    memorize_many_cdb_time = timeit.timeit('memorize_many_cdb(collection3)', 
                        setup='''
import chromadb
from chromadb.utils import embedding_functions
from __main__ import memorize_many_cdb
client = chromadb.Client()
collection3 = client.create_collection(name="collection3")
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE MANY CDB")
    
    memorize_many_pc_time = timeit.timeit('memorize_many_pc(index)', 
                        setup='''
from pinecone import Pinecone, PodSpec
import os
from dotenv import load_dotenv
from __main__ import memorize_many_pc
load_dotenv(dotenv_path='.env', verbose=True)
pc = Pinecone(api_key=os.getenv('PC_API_KEY'))
for i in pc.list_indexes():
    if i['name'] == "quickstart":
        pc.delete_index(i['name'])
pc.create_index(name="quickstart", dimension=384, metric="cosine", spec=PodSpec(environment='gcp-starter'))
index = pc.Index("quickstart")
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE MANY PC")

    memorize_many_w_time = timeit.timeit('memorize_many_w(client)', 
                        setup='''
import weaviate
import weaviate.classes as wvc
import os
from dotenv import load_dotenv
from __main__ import memorize_many_w
load_dotenv(dotenv_path='.env', verbose=True)
client = weaviate.Client(
    url = "https://test-i6cwsfxe.weaviate.network",
    auth_client_secret=weaviate.auth.AuthApiKey(api_key=os.getenv('W_API_KEY')),
)
class_obj = {
    "class": "Question",
    "vectorizer": "none",
}
client.schema.delete_class("Question")
client.schema.create_class(class_obj)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE MANY W")

    remember_many_v1_time = timeit.timeit('remember_v1(v, text)', 
                        setup='''
from vlite import VLite
from __main__ import remember_v1, memorize_many_v1
v = VLite()
memorize_many_v1(v)
text = "civil law"
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER MANY V1")
    
    remember_many_v2_time = timeit.timeit('remember_v2(v, "civil law")', 
                        setup='''
from vlite2 import VLite2
from __main__ import remember_v2, memorize_many_v2
v = VLite2()
memorize_many_v2(v)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER MANY V2")

    remember_many_cdb_time = timeit.timeit('remember_cdb(collection4, "civil law")', 
                        setup='''
import chromadb
from chromadb.utils import embedding_functions
from __main__ import memorize_many_cdb, remember_cdb
client = chromadb.Client()
collection4 = client.create_collection(name="collection4")
memorize_many_cdb(collection4)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER MANY CDB")

    remember_many_pc_time = timeit.timeit('remember_pc(index, "civil law")', 
                        setup='''
from pinecone import Pinecone, PodSpec
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv
from __main__ import memorize_many_pc, remember_pc
load_dotenv(dotenv_path='.env', verbose=True)
pc = Pinecone(api_key=os.getenv('PC_API_KEY'))
for i in pc.list_indexes():
    if i['name'] == "quickstart":
        pc.delete_index(i['name'])
pc.create_index(name="quickstart", dimension=384, metric="cosine", spec=PodSpec(environment='gcp-starter'))
index = pc.Index("quickstart")
memorize_many_pc(index)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER MANY PC")

    remember_many_w_time = timeit.timeit('remember_w(client, "civil law")', 
                        setup='''
import weaviate
import weaviate.classes as wvc
import os
from dotenv import load_dotenv
from __main__ import memorize_many_w, remember_w
load_dotenv(dotenv_path='.env', verbose=True)
client = weaviate.Client(
    url = "https://test-i6cwsfxe.weaviate.network",
    auth_client_secret=weaviate.auth.AuthApiKey(api_key=os.getenv('W_API_KEY')),
)
class_obj = {
    "class": "Question",
    "vectorizer": "none",
}
client.schema.delete_class("Question")
client.schema.create_class(class_obj)
memorize_many_w(client)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER MANY W")
    
    print(f"\n\nNumber of executions averaged over: {num_executions}")
    print(f"v1 memorize one: {memorize_one_v1_time}")
    print(f"v2 memorize one: {memorize_one_v2_time}")
    print(f"cdb memorize one: {memorize_one_cdb_time}")
    print(f"pc memorize one: {memorize_one_pc_time}")
    print(f"w memorize one: {memorize_one_w_time}")
    print(f"v1 remember one: {remember_one_v1_time}")
    print(f"v2 remember one: {remember_one_v2_time}")
    print(f"cdb remember one: {remember_one_cdb_time}")
    print(f"pc remember one: {remember_one_pc_time}")
    print(f"w remember one: {remember_one_w_time}")
    print(f"v1 memorize many: {memorize_many_v1_time}")
    print(f"v2 memorize many: {memorize_many_v2_time}")
    print(f"cdb memorize many: {memorize_many_cdb_time}")
    print(f"pc memorize many: {memorize_many_pc_time}")
    print(f"w mmemorize many: {memorize_many_w_time}")
    print(f"v1 remember many: {remember_many_v1_time}")
    print(f"v2 remember many: {remember_many_v2_time}")
    print(f"cdb remember many: {remember_many_cdb_time}")
    print(f"pc remember many: {remember_many_pc_time}")
    print(f"w remember many: {remember_many_w_time}\n\n")

    files_to_delete = glob.glob('*.npz')
    files_to_delete += glob.glob('*.info')
    files_to_delete += glob.glob('*.index')
    for f in files_to_delete:
        os.remove(f)
    load_dotenv(dotenv_path='.env', verbose=True)
    pc = Pinecone(api_key=os.getenv('PC_API_KEY'))
    for i in pc.list_indexes():
        if i['name'] == "quickstart":
            pc.delete_index(i['name'])
    client = weaviate.Client(
    url = "https://test-i6cwsfxe.weaviate.network",
    auth_client_secret=weaviate.auth.AuthApiKey(api_key=os.getenv('W_API_KEY')),
    )
    client.schema.delete_class("Question")


    end_time = time.time()
    print(f"Total time to run: {end_time - start_time} seconds")
    