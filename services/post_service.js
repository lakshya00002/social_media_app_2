const Post = require('../models/post');

class PostService {
  async getAllPosts() {
    return await Post.find().populate('user_id', 'username').sort({ created_at: -1 });
  }

  async getPostById(postId) {
    const post = await Post.findById(postId).populate('user_id', 'username');
    if (!post) {
      throw new Error('Post not found');
    }
    return post;
  }

  async createPost(userId, content) {
    const post = new Post({ user_id: userId, content });
    await post.save();
    return post;
  }

  async updatePost(postId, content) {
    const post = await Post.findById(postId);
    if (!post) {
      throw new Error('Post not found');
    }
    post.content = content;
    post.updated_at = new Date();
    await post.save();
    return post;
  }

  async deletePost(postId) {
    const post = await Post.findByIdAndDelete(postId);
    if (!post) {
      throw new Error('Post not found');
    }
    return post;
  }
}

module.exports = new PostService();
