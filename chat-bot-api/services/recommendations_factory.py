from models import UserMessage, AIMessage, ChatSession, ChatHistory, UserInteractionInfo, Recommendation
import util as ut
import pandas as pd


def cosine_similarity(text1, text2):
  from sklearn.feature_extraction.text import CountVectorizer
  from sklearn.metrics.pairwise import cosine_similarity

  vectorizer = CountVectorizer()
  X = vectorizer.fit_transform([text1, text2])
  return cosine_similarity(X[0], X[1])[0][0]


class RecommendationsFactory:
  def __init__(self, ctx):
    self.ctx = ctx


  async def create(self, raw_recommendations, email, base_url):
    recommendations = []

    for r in list(raw_recommendations):
      sim_items, distances = await self.ctx.item_service.find_by_title(r['title'], limit=1)

      if distances[0] < 0:
        continue

      total_sim = 1 - distances[0]

      if total_sim > 0.1:
        item = sim_items[0]

        title_sim = cosine_similarity(r['title'], item.title.strip())

        if title_sim >= 0.5:
          recommendations.append(Recommendation(
            title         = r['title'],
            release       = r['release'],
            description   = r['description'],
            rating        = r['rating'],
            votes         = [ f'{base_url}api/v1/interactions/make/{email}/{item.id}/{i}' for i in range(1, 6)],
            total_sim     = total_sim,
            db_title_sim  = title_sim,
            db_title      = item.title.strip()
          ))

    return recommendations
