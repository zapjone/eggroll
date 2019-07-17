/*
 * Copyright 2019 The Eggroll Authors. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.webank.ai.eggroll.framework.meta.service.dao.generated.mapper;

import com.webank.ai.eggroll.framework.meta.service.dao.generated.model.Result;
import com.webank.ai.eggroll.framework.meta.service.dao.generated.model.ResultExample;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.session.RowBounds;

import java.util.List;

public interface ResultMapper {
    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table result
     *
     * @mbg.generated
     */
    long countByExample(ResultExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table result
     *
     * @mbg.generated
     */
    int deleteByExample(ResultExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table result
     *
     * @mbg.generated
     */
    int deleteByPrimaryKey(Long resultId);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table result
     *
     * @mbg.generated
     */
    int insert(Result record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table result
     *
     * @mbg.generated
     */
    int insertSelective(Result record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table result
     *
     * @mbg.generated
     */
    List<Result> selectByExampleWithRowbounds(ResultExample example, RowBounds rowBounds);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table result
     *
     * @mbg.generated
     */
    List<Result> selectByExample(ResultExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table result
     *
     * @mbg.generated
     */
    Result selectByPrimaryKey(Long resultId);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table result
     *
     * @mbg.generated
     */
    int updateByExampleSelective(@Param("record") Result record, @Param("example") ResultExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table result
     *
     * @mbg.generated
     */
    int updateByExample(@Param("record") Result record, @Param("example") ResultExample example);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table result
     *
     * @mbg.generated
     */
    int updateByPrimaryKeySelective(Result record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table result
     *
     * @mbg.generated
     */
    int updateByPrimaryKey(Result record);
}